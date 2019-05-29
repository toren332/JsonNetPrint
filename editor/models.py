from django.db import models
from rest_framework import serializers
# from django.core.exceptions import ValidationError


class Section(models.Model):
    """Section"""
    title = models.CharField('title', max_length=40, blank=False)

    def __str__(self):
        return self.title


class Page(models.Model):
    """Description pages"""
    text = models.CharField(max_length=2048)
    image = models.URLField(max_length=2048)
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class ItemPhotoVariant(models.Model):
    """Photo item variant"""
    size_width = models.PositiveIntegerField(default=0)
    size_height = models.PositiveIntegerField(default=0)
    uncutted_size_width = models.PositiveIntegerField(default=0)
    uncutted_size_height = models.PositiveIntegerField(default=0)
    dpi = models.PositiveIntegerField(default=300)
    oms_id = models.CharField(max_length=256)
    paper_CHOICES = (
        ('standart_matte', 'standart_matte'),
        ('standart_glossy', 'standart_glossy'),
        ('premium_matte', 'premium_matte'),
        ('premium_glossy', 'premium_glossy'),
        ('metallic', 'metallic'),
    )
    paper = models.CharField(max_length=256, choices=paper_CHOICES)
    bordered_image = models.URLField(max_length=2048, blank=True)
    image = models.URLField(max_length=2048)
    image_region_top = models.PositiveIntegerField(default=0)
    image_region_width = models.PositiveIntegerField(default=0)
    image_region_left = models.PositiveIntegerField(default=0)
    image_region_height = models.PositiveIntegerField(default=0)
    image_region_angle = models.FloatField(default=0)
    bordered_image_region_top = models.PositiveIntegerField(default=0)
    bordered_image_region_width = models.PositiveIntegerField(default=0)
    bordered_image_region_left = models.PositiveIntegerField(default=0)
    bordered_image_region_height = models.PositiveIntegerField(default=0)
    bordered_image_region_angle = models.FloatField(default=0)
    text_region_top = models.PositiveIntegerField(default=0, blank=True)
    text_region_width = models.PositiveIntegerField(default=0, blank=True)
    text_region_left = models.PositiveIntegerField(default=0, blank=True)
    text_region_height = models.PositiveIntegerField(default=0, blank=True)
    text_region_angle = models.FloatField(default=0, blank=True)
    font_size = models.FloatField(default=0, blank=True)
    default_frame_orientation_CHOICES = (
        ('top', 'top'),
        ('bottom', 'bottom'),
        ('left', 'left'),
        ('right', 'right'),
    )
    default_frame_orientation = models.CharField(max_length=128, choices=default_frame_orientation_CHOICES)
    is_orientation_switch_allowed = models.BooleanField(default=True)
    is_colored = models.BooleanField(default=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.oms_id + ' ' + self.paper


class ItemPhoto(models.Model):
    """ItemPhoto"""
    comment = models.CharField(max_length=2048)
    item_photo_variant_0 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v0', blank=False)
    item_photo_variant_1 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v1', blank=True, null=True)
    item_photo_variant_2 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v2', blank=True, null=True)
    item_photo_variant_3 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v3', blank=True, null=True)
    item_photo_variant_4 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v4', blank=True, null=True)
    item_photo_variant_5 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v5', blank=True, null=True)
    item_photo_variant_6 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v6', blank=True, null=True)
    item_photo_variant_7 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v7', blank=True, null=True)
    item_photo_variant_8 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v8', blank=True, null=True)
    item_photo_variant_9 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v9', blank=True, null=True)
    item_photo_variant_10 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v10', blank=True, null=True)
    item_photo_variant_11 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v11', blank=True, null=True)
    item_photo_variant_12 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v12', blank=True, null=True)
    item_photo_variant_13 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v13', blank=True, null=True)
    item_photo_variant_14 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v14', blank=True, null=True)
    item_photo_variant_15 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v15', blank=True, null=True)
    item_photo_variant_16 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v16', blank=True, null=True)
    item_photo_variant_17 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v17', blank=True, null=True)
    item_photo_variant_18 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v18', blank=True, null=True)
    item_photo_variant_19 = models.ForeignKey(ItemPhotoVariant, on_delete=models.CASCADE, related_name='v19', blank=True, null=True)
    base_variant = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.comment


class PageTemplate(models.Model):
    """PageTemplate variant"""
    width = models.FloatField(default=0)
    top = models.FloatField(default=0)
    left = models.FloatField(default=0)
    height = models.FloatField(default=0)
    angle = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.width) + ' ' + str(self.height)


class CoverTemplate(models.Model):
    """CoverTemplate variant"""
    width = models.FloatField(default=0)
    top = models.FloatField(default=0)
    left = models.FloatField(default=0)
    height = models.FloatField(default=0)
    angle = models.PositiveIntegerField(default=0)
    text_region_top = models.PositiveIntegerField(default=0, blank=True)
    text_region_width = models.PositiveIntegerField(default=0, blank=True)
    text_region_left = models.PositiveIntegerField(default=0, blank=True)
    text_region_height = models.PositiveIntegerField(default=0, blank=True)
    text_region_angle = models.FloatField(default=0, blank=True)
    font_size = models.FloatField(default=0, blank=True)
    def __str__(self):
        return str(self.width) + ' ' + str(self.height)


class ItemBook(models.Model):
    """ItemBook"""
    base_variant_id = models.PositiveIntegerField(default=0)
    comment = models.CharField(max_length=2048)
    paper_CHOICES = (
        ('standart_matte', 'standart_matte'),
        ('standart_glossy', 'standart_glossy'),
        ('premium_matte', 'premium_matte'),
        ('premium_glossy', 'premium_glossy'),
        ('metallic', 'metallic'),
    )
    paper = models.CharField(max_length=256, choices=paper_CHOICES)
    additional_turn_price = models.PositiveIntegerField(default=0)
    variant_comment = models.CharField(max_length=2048)
    cover_dpi = models.PositiveIntegerField(default=300)
    cover_oms_id = models.CharField(max_length=2048)
    page_oms_id = models.CharField(max_length=2048)
    page_dpi = models.PositiveIntegerField(default=300)
    min_page_count = models.PositiveIntegerField(default=20)
    max_page_count = models.PositiveIntegerField(default=120)
    price = models.PositiveIntegerField(default=0)

    uncutted_page_size_width = models.PositiveIntegerField(default=0)
    uncutted_page_size_height = models.PositiveIntegerField(default=0)
    cover_size_width = models.PositiveIntegerField(default=0)
    cover_size_height = models.PositiveIntegerField(default=0)
    uncutted_cover_size_width = models.PositiveIntegerField(default=0)
    uncutted_cover_size_height = models.PositiveIntegerField(default=0)
    cover_turn_size_width = models.PositiveIntegerField(default=0)
    cover_turn_size_height = models.PositiveIntegerField(default=0)
    uncutted_cover_turn_size_width = models.PositiveIntegerField(default=0)
    uncutted_cover_turn_size_height = models.PositiveIntegerField(default=0)
    page_size_width = models.PositiveIntegerField(default=0)
    page_size_height = models.PositiveIntegerField(default=0)

    item_book_page_0 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt0', blank=False)
    item_book_page_1 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt1', blank=True, null=True)
    item_book_page_2 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt2', blank=True, null=True)
    item_book_page_3 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt3', blank=True, null=True)
    item_book_page_4 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt4', blank=True, null=True)
    item_book_page_5 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt5', blank=True, null=True)
    item_book_page_6 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt6', blank=True, null=True)
    item_book_page_7 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt7', blank=True, null=True)
    item_book_page_8 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt8', blank=True, null=True)
    item_book_page_9 = models.ForeignKey(PageTemplate, on_delete=models.CASCADE, related_name='pt9', blank=True, null=True)
    base_page_template_id = models.PositiveIntegerField(default=0)

    item_book_cover_0 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct0', blank=False)
    item_book_cover_1 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct1', blank=True, null=True)
    item_book_cover_2 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct2', blank=True, null=True)
    item_book_cover_3 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct3', blank=True, null=True)
    item_book_cover_4 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct4', blank=True, null=True)
    item_book_cover_5 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct5', blank=True, null=True)
    item_book_cover_6 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct6', blank=True, null=True)
    item_book_cover_7 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct7', blank=True, null=True)
    item_book_cover_8 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct8', blank=True, null=True)
    item_book_cover_9 = models.ForeignKey(CoverTemplate, on_delete=models.CASCADE, related_name='ct9', blank=True, null=True)
    base_cover_template_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.comment


class Entries(models.Model):
    """Section entries"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    id_name = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description_title = models.CharField(max_length=256)
    cover_image = models.URLField(max_length=2048)
    page_0 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p0')
    page_1 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p1', blank=True, null=True)
    page_2 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p2', blank=True, null=True)
    page_3 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p3', blank=True, null=True)
    page_4 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p4', blank=True, null=True)
    page_5 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p5', blank=True, null=True)
    page_6 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p6', blank=True, null=True)
    page_7 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p7', blank=True, null=True)
    page_8 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p8', blank=True, null=True)
    page_9 = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='p9', blank=True, null=True)
    item_id_PHOTO = models.ForeignKey(ItemPhoto, on_delete=models.CASCADE, blank=True, null=True)
    item_id_BOOK = models.ForeignKey(ItemBook, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.id_name + '(' + self.section.title + ')'


class Json(models.Model):
    """ItemBook"""
    name = models.CharField(max_length=2048)
    version = models.PositiveIntegerField(default=2)

    json = models.CharField(max_length=1048576)

    def __str__(self):
        return self.name + ' v' + str(self.version)
