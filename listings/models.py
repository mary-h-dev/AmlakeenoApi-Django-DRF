from django.contrib.gis.db import models
from random import choices
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model

User = get_user_model()

import PIL
from django.core.files import File
from io import BytesIO

"""
compress images
"""
def compress(picture):
    if picture:
        pic = PIL.Image.open(picture)
        buf = BytesIO()
        pic.save(buf, "JPEG", quality=35)
        new_pic = File(buf, name=picture.name)
        return new_pic
    else:
        return None


class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    choices_bargain_type = (
        ("فروش", "فروش"),
        ("اجاره", "اجاره"),
        ("رهن کامل", "رهن کامل"),
    )
    bargain_type = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_bargain_type
    )


    choices_listing_type = (
        ("مسکونی", "مسکونی"),
        ("اداری", "اداری"),
        ("تجاری", "تجاری"),
    )
    listing_type = models.CharField(
        max_length=20, choices=choices_listing_type, blank=True, null=True
    )


    choices_property_type = (
        ("ویلایی", "ویلایی"),
        ("آپارتمان", "آپارتمان"),
        ("مغازه","مغازه"),
    )
    property_type = models.CharField(
        max_length=20, choices=choices_property_type, blank=True, null=True
    )

    # the area
    choices_area = (("تهران", "تهران"),)
    area = models.CharField(max_length=20, blank=True, null=True, choices=choices_area)
    borough = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    area_metere = models.DecimalField(
        max_digits=50, decimal_places=0, blank=True, null=True
    )
    age_of_building = models.IntegerField(blank=True, null=True)
    price_for_sale = models.DecimalField(
        max_digits=50, decimal_places=0,default=0, null=True, blank=True
    )
 
    rent_per_month = models.DecimalField(
        max_digits=50, decimal_places=0, default=0, null=True, blank=True
    )
    number_of_floor_of_building = models.IntegerField(blank=True, null=True)
    number_of_unit_per_floor = models.IntegerField(blank=True, null=True)
    floor_of_building = models.IntegerField(blank=True, null=True)
    name_of_property_owner = models.CharField(max_length=30, blank=True, null=True)
    address_of_building = models.TextField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)

    # facilites
    pool = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    lobby = models.BooleanField(default=False)
    guard = models.BooleanField(default=False)
    warehouse = models.BooleanField(default=False)
    Jacuzzi = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    choices_property_status = (
        ("تخلیه", "تخلیه"),
        ("در دست مستاجر", "در دست مستاجر"),
        ("در دست صاحب ملک", "در دست صاحب ملک"),
    )
    property_status = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_property_status
    )

    choices_building_face = (
        ("شمالی", "شمالی"),
        ("جنوبی", "جنوبی"),
        ("شرقی", "شرقی"),
        ("غربی", "غربی"),
    )
    building_face = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_building_face
    )

    choices_room_number = (
        ("یک اتاق", "یک اتاق"),
        ("دو اتاق", "دو اتاق"),
        ("سه اتاق", "سه اتاق"),
        ("چهار اتاق", "چهار اتاق"),
        ("بیشتر از چهار اتاق", "بیشتر از چهار اتاق"),
    )
    rooms = models.CharField(
        max_length=30, choices=choices_room_number, blank=True, null=True
    )

    choices_building_apearence = (
        ("سنگ", "سنگ"),
        ("آجر سه سانتی", "آجر سه سانتی"),
        ("ترکیبی", "ترکیبی"),
        ("رومی", "رومی"),
        ("آجر و سیمان", "آجر و سیمان"),
        ("سیمان", "سیمان"),
        ("سایر", "سایر"),
    )
    building_apearence = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_building_apearence
    )

    choices_floor_covering = (
        ("پارکت", "پارکت"),
        ("موکت", "موکت"),
        ("لمینت", "لمینت"),
        ("سرامیک", "سرامیک"),
        ("سنگ", "سنگ"),
        ("سایر", "سایر"),
    )
    floor_covering = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_floor_covering
    )

    choices_kitchen_apearence = (
        ("MDF", "MDF"),
        ("هایگلاس", "هایگلاس"),
        ("فلزی", "فلزی"),
        ("سایر", "سایر"),
    )
    kitchen_apearence = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_kitchen_apearence
    )

    choices_wc_type = (
        ("ایرانی", "ایرانی"),
        ("فرنگی", "فرنگی"),
        ("ایرانی-فرنگی", "ایرانی-فرنگی"),
    )
    wc_type = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_wc_type
    )

    choices_heating_system = (
        ("شوفاژ", "شوفاژ"),
        ("پکیج", "پکیج"),
        ("بخاری", "بخاری"),
        ("سایر", "سایر"),
    )
    heating_system = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_heating_system
    )

    choices_cooling_system = (
        ("کولر گازی", "کولر گازی"),
        ("کولر آبی", "کولر آبی"),
        ("چیلر", "چیلر"),
        ("فن کوئل", "فن کوئل"),
        ("اسپلیت", "اسپلیت"),
        ("سایر", "سایر"),
    )
    cooling_system = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_cooling_system
    )

    choices_house_document_status = (
        ("",""),
        ("شخصی", "شخصی"),
        ("قولنامه", "قولنامه"),
        ("بنیادی", "بنیادی"),
        ("زمین شهری", "زمین شهری"),
        ("فرمان امام", "فرمان امام"),
        ("اوقافی", "اوقافی"),
        ("تعاونی", "تعاونی"),
        ("سایر", "سایر"),
    )
    house_document_status = models.CharField(
        max_length=40, blank=True, null=True, choices=choices_house_document_status
    )

    choices_house_document_type = (
        ("",""),
        ("مسکونی", "مسکونی"),
        ("اداری", "اداری"),
        ("تجاری", "تجاری"),
        ("سایر", "سایر"),
    )
    house_document_type = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_house_document_type
    )

    choices_advertiser_type = (
        ("شخص", "شخص"),
        ("املاک", "املاک"),
    )
    advertiser = models.CharField(
        max_length=20, choices=choices_advertiser_type, blank=True, null=True
    )

    # pictures
    picture1 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    picture2 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    picture3 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    picture4 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    picture5 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    picture6 = models.ImageField(blank=True, null=True, upload_to="picture6/%Y/%m/%d")

    def __str__(self):
        return self.listing_type

    def save(self, *args, **kwargs):
        new_picture1 = compress(self.picture1)
        self.picture1 = new_picture1

        new_picture2 = compress(self.picture2)
        self.picture2 = new_picture2

        new_picture3 = compress(self.picture3)
        self.picture3 = new_picture3

        new_picture4 = compress(self.picture4)
        self.picture4 = new_picture4

        new_picture5 = compress(self.picture5)
        self.picture5 = new_picture5

        new_picture6 = compress(self.picture6)
        self.picture6 = new_picture6

        super().save(*args, **kwargs)




class Poi(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    choices_type = (
        ("دانشگاه", "دانشگاه"),
        ("بیمارستان", "بیمارستان"),
        ("استادیوم", "استادیوم"),
    )
    type = models.CharField(max_length=50, choices=choices_type)
    location = models.PointField(srid=4326, blank=True, null=True)

    def __str__(self):
        return self.name
    



