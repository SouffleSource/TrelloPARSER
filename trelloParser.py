import json
import sys

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_card_details(data):
    cards = {}
    for card in data['cards']:
        cards[card['id']] = {
            'name': card['name'],
            'desc': card['desc'],
            'link': card['url']
        }
    return cards

def add_comments_to_cards(cards, data):
    for action in data['actions']:
        if action['type'] == 'commentCard' and action['data']['card']['id'] in cards:
            card_id = action['data']['card']['id']
            if 'comments' not in cards[card_id]:
                cards[card_id]['comments'] = []
            cards[card_id]['comments'].append(action['data']['text'])

def categorise_cards(cards):
    reformatted = {
        'active': [card for card in cards.values() if card.get('comments')],
        'inactive': [card for card in cards.values() if not card.get('comments') and card.get('createDate') is None]
    }
    return reformatted

def write_data_to_json(data, filename='trelloData.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def ensure_consistent_format(cards):
    for card in cards:
        if 'createDate' not in card:
            card['createDate'] = None
        if 'copyDate' not in card:
            card['copyDate'] = None
        if 'comments' not in card:
            card['comments'] = []
        if card['createDate'] is None:
            card['createDate'] = card['copyDate']
        del card['copyDate']

        card_keys = ['name', 'desc', 'link', 'createDate', 'comments']
        card.update({key: card.get(key) for key in card_keys})

def add_card_dates(cards, data):
    for action in data['actions']:
        if action['type'] in ['copyCard', 'createCard']:
            card_id = action['data']['card']['id']
            if card_id in cards:
                if action['type'] == 'createCard':
                    cards[card_id]['createDate'] = action['date']
                elif action['type'] == 'copyCard' and 'createDate' not in cards[card_id]:
                    cards[card_id]['createDate'] = action['date']


def main():
    if len(sys.argv) < 2:
        print("Usage: python trelloParser.py <path_to_your_trello_export.json>")
        sys.exit(1)
    input_file_path = sys.argv[1]
    data = load_data(input_file_path)
    cards = extract_card_details(data)
    add_card_dates(cards, data)
    add_comments_to_cards(cards, data)
    cards_list = [{'id': card_id, **card_details} for card_id, card_details in cards.items()]
    ensure_consistent_format(cards_list)
    categorised_cards = categorise_cards(cards)
    write_data_to_json(categorised_cards)

if __name__ == '__main__':
    main()