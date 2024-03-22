from django.contrib import admin

from .models import Listing, Realtor, Amenity, Rules_Terms, Address
admin.site.register(Realtor)
admin.site.register(Amenity)
admin.site.register(Rules_Terms)
admin.site.register(Address)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_available', 'list_date', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('amenities',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'zipcode', 'description', 'bedrooms', 'sqft', 'state')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)