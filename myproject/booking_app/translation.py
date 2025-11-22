from .models import Hotel, UserProfile, City, Room, Review, Country
from modeltranslation.translator import TranslationOptions,register


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
      fields = ('first_name', 'last_name')

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
     fields = ('street', 'description')


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)





