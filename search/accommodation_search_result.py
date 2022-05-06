BOOKING_IMAGE_PREFIX = 'https://t-cf.bstatic.com/'


class AccommodationSearchResult:
    def __init__(self, _dict: dict):
        self.name: str = _dict.get('displayName').get('text')
        self.id: int = int(_dict.get('basicPropertyData').get('__ref').split(':')[1])
        location_dict = _dict.get('location')
        self.location: str = location_dict.get('displayLocation')
        self.main_distance: str = location_dict.get('mainDistance')

        try:
            self.price: str = _dict.get('priceDisplayInfo').get('priceBeforeDiscount').get('amountPerStay').get(
                'amountRounded')
        except AttributeError as e:
            self.price = '0.00 zł'

        self.image_url: str = ''
        self.stars: int = -1
        self.review_score: float = 0.0

    def add_extra_info(self, _extra_dict: dict):
        self.image_url = BOOKING_IMAGE_PREFIX + _extra_dict.get('photos').get('main').get('highResJpegUrl').get(
            'relativeUrl')
        self.review_score = _extra_dict.get('reviews').get('totalScore')

        try:
            star_rating = _extra_dict.get('starRating')
            if star_rating != -1:
                self.stars = star_rating.get('value')
            else:
                print(self.id)
        except AttributeError:
            # some accommodation could not have a star
            pass

    def __repr__(self):
        return f'{self.id}'
