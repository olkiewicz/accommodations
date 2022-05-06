import json

import requests

from search.accommodation_search_result import AccommodationSearchResult


def get_city_destination_id(destination_response: dict) -> int:
    for number, result in enumerate(destination_response.get('results')):
        dest_type = result.get('dest_type')

        if dest_type == 'city':
            return result.get('dest_id')


def get_booking_destination_id(place: str):
    payload = {"query": place, "pageview_id": "c70098672b8a01c1", "aid": 304142, "language": "pl", "size": 5}
    response = requests.post('https://accommodations.booking.com/autocomplete.json', data=json.dumps(payload))
    encoded_response_dest_response = json.loads(response.text)

    return get_city_destination_id(encoded_response_dest_response)


def booking_request_with_place_and_date(place: str, checkin: str, checkout: str):
    dest_id = get_booking_destination_id(place)

    url = f'https://www.booking.com/searchresults.pl.html?ss={place}&ssne=Warszawa&ssne_untouched=Warszawa&label=gen173nr-1DCAEoggI46AdIM1gEaLYBiAEBmAEeuAEXyAEM2AED6AEB-AEDiAIBqAIDuALU-LCTBsACAdICJDZlOGNjMDRjLTM0ZmQtNDFmMS1iYjRhLTgxNzA2ZTcxZGU4NtgCBOACAQ&sid=120e8f45ece47d36fff8195dcefb9040&aid=304142&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id={dest_id}&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&checkin={checkin}&checkout={checkout}&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'Cookie': 'cors_js=1; OptanonAlertBoxClosed=2021-05-16T08:50:20.409Z; 11_srd=%7B%22features%22%3A%5B%7B%22id%22%3A9%7D%5D%2C%22score%22%3A3%2C%22detected%22%3Afalse%7D; pc_payer_id=936c242e-e049-469d-9952-98b9ff830749; clba=1; bs=%7B%22gc%22%3A1%7D; _pxhd=OlgRkZxxSbufORUFYa5C6YkSVEprGfBAUrckQXLnteE2VFU8S4v2kqzkSHOrUD4f4r3sWwOQ0sBdfX%2Fqk5shpg%3D%3D%3AS-XxiqIBQKaBI5gQMkegdaTRygCySuqxLcjmRZUbBCb-jMebuTgFF5Wv3M%2F1WuyVr6UCG64QbaaVwNM3%2FEW14bV1vDLyteLLjrIBFJtMick%3D; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siaCI6IlJGMk16SStmSTBWY3d3TGFqWlNBaVR2cXZ3R3NSajI5L0pWZ0g2M2FjMVkifV19; _pxhd=MwxnrmxkEPJoszItoLTtsZf2E8Lw9Okz9dln%2FDjK8xyCTyoM34dPCOsG2vwnIJMJpqC0WqNji1rnHNw%2FigrPkw%3D%3D%3AxSjVtS6YHeSa1jorrPqBDIy2u-iaYPu%2FmtRZT5wSm5y2kJCjdR7MPniQxBgOHTeieKAgFQfWiKgYeWEssLMsHSZM18kq0pnbXb8IKZJ1uEg%3D; bkng_frontend_sese_exp=0; bkng_expired_hint=eyJib29raW5nX2dsb2JhbCI6W3sibG9naW5faGludCI6MTMyNTUxMjQ1OX1dfQ; bkng_sso_session=e30; OptanonConsent=isIABGlobal=false&datestamp=Fri+Apr+29+2022+21%3A28%3A11+GMT%2B0200+(czas+%C5%9Brodkowoeuropejski+letni)&version=6.22.0&hosts=&consentId=6193ffb9-f707-4248-89e3-6ddf34a0601a&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A0&geolocation=PL%3B04&AwaitingReconsent=false&backfilled_at=1629450978980&isGpcEnabled=0&implicitConsentCountry=GDPR&implicitConsentDate=1637760044650; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbpAcOBknrMeR4Ym2gxOcV%2BDx5P5WCnIE2oMDe%2FQ%2FvAqvPOKa949xaVEtL6FLgQ2klUvKLg0xDqaT0WiTsvFGUT9W%2FCUfS1%2FGJo7KGoMMCY0YOpeGSAM3a2KDPCu7somPVyoCESHZxalv8i6%2BuyLmusRXIX8yF0ofLxfKx%2ByFkiHio33Wvj6K1AKbScz4qgriBTVcxR6CDryp8CH48LqWyx4PBEukQWRrg; lastSeen=0',
        'Referer': 'https://www.booking.com/index.pl.html?label=gen173nr-1DCAEoggI46AdIM1gEaLYBiAEBmAEeuAEXyAEM2AED6AEB-AEDiAIBqAIDuALU-LCTBsACAdICJDZlOGNjMDRjLTM0ZmQtNDFmMS1iYjRhLTgxNzA2ZTcxZGU4NtgCBOACAQ;sid=120e8f45ece47d36fff8195dcefb9040;keep_landing=1&sb_price_type=total&'
    }

    return requests.get(url, headers=headers)


def handle_booking_response(response: str):
    result_start_index = response.index('"results"')
    result_end_index = response.index('"searchMeta"') - 1
    content = '{' + response[result_start_index:result_end_index] + '}'
    search_results = json.loads(content).get('results')

    extra_info_start_index = response.index('"BasicPropertyData:') - 1
    extra_info_end_index = response.index('"ROOT_QUERY"') - 1
    extra_info_content = response[extra_info_start_index:extra_info_end_index] + '}'
    extra_info_results = json.loads(extra_info_content)

    accommodations = []
    for search_result in search_results:
        accommodation = AccommodationSearchResult(search_result)
        accommodations.append(accommodation)

        for extra_info in extra_info_results.values():
            if extra_info.get('__typename') == 'BasicPropertyData':
                if extra_info.get('id') == accommodation.id:
                    accommodation.add_extra_info(extra_info)

    return accommodations


def get_results(place):
    results = booking_request_with_place_and_date(place, '2022-09-22', '2022-09-23')
    encoded_results = handle_booking_response(results.text)

    return encoded_results
