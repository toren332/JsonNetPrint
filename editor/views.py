from django.shortcuts import render
from . import serializers, models
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import json


class JsonViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['POST'])
    def create_json(self, request):
        version = request.data['version']
        response = {}

        if version == '2':
            sections = []
            for section_model in models.Section.objects.all():
                section = {}
                section['title'] = section_model.title
                entries = []
                for entry_model in models.Entries.objects.filter(section=section_model):
                    entries.append(entry_model.id)
                section['entries'] = entries
                sections.append(section)
            entries = []
            for entry_model in models.Entries.objects.all():
                entry = {}
                entry['id'] = entry_model.id_name
                entry['subtitle'] = entry_model.subtitle
                entry['title'] = entry_model.title
                entry['cover_image'] = entry_model.cover_image
                page_models_list = [
                    entry_model.page_0,
                    entry_model.page_1,
                    entry_model.page_2,
                    entry_model.page_3,
                    entry_model.page_4,
                    entry_model.page_5,
                    entry_model.page_6,
                    entry_model.page_7,
                    entry_model.page_8,
                    entry_model.page_9,
                ]
                pages = []
                for page_model in page_models_list:
                    if page_model:
                        page = {}
                        page['text'] = page_model.text
                        page['title'] = page_model.title
                        page['image'] = page_model.image
                        pages.append(page)
                entry['description'] = {'title': entry_model.description_title, 'pages': pages}

                entry['id'] = entry_model.id_name
                if entry_model.item_id_PHOTO_id is None and entry_model.item_id_BOOK_id is None:
                    return Response({"ERROR": "no photo or book id in entries in" + str(entry_model.id_name)}, status=status.HTTP_409_CONFLICT)
                else:
                    if entry_model.item_id_PHOTO_id is not None and entry_model.item_id_BOOK_id is not None:
                        return Response({"ERROR": "photo and book id in entries, choose one"},
                                        status=status.HTTP_409_CONFLICT)
                    else:
                        if entry_model.item_id_PHOTO_id is not None:
                            entry['item_id'] = entry_model.item_id_PHOTO_id
                        else:
                            entry['item_id'] = entry_model.item_id_BOOK_id

                entries.append(entry)
            items = []
            _ = 0
            for photo_model in models.ItemPhoto.objects.all():
                item = {}
                item['id'] = _
                item['comment'] = photo_model.comment

                photo_model_variant_list = [
                    photo_model.item_photo_variant_0,
                    photo_model.item_photo_variant_1,
                    photo_model.item_photo_variant_2,
                    photo_model.item_photo_variant_3,
                    photo_model.item_photo_variant_4,
                    photo_model.item_photo_variant_5,
                    photo_model.item_photo_variant_6,
                    photo_model.item_photo_variant_7,
                    photo_model.item_photo_variant_8,
                    photo_model.item_photo_variant_9,
                    photo_model.item_photo_variant_10,
                    photo_model.item_photo_variant_11,
                    photo_model.item_photo_variant_12,
                    photo_model.item_photo_variant_13,
                    photo_model.item_photo_variant_14,
                    photo_model.item_photo_variant_15,
                    photo_model.item_photo_variant_16,
                    photo_model.item_photo_variant_17,
                    photo_model.item_photo_variant_18,
                    photo_model.item_photo_variant_19,
                ]
                photo_variants = []
                type = {}
                type['base_variant_id'] = photo_model.base_variant
                tmp_ = 0
                for photo_variant_model in photo_model_variant_list:
                    if photo_variant_model:
                        photo_variant = {}
                        size = {
                            'width': photo_variant_model.size_width,
                            'height': photo_variant_model.size_height
                        }
                        photo_variant['size'] = size
                        uncutted_size = {
                            'width': photo_variant_model.uncutted_size_width,
                            'height': photo_variant_model.uncutted_size_height
                        }
                        photo_variant['id'] = tmp_
                        photo_variant['uncutted_size'] = uncutted_size
                        photo_variant['oms_id'] = photo_variant_model.oms_id
                        photo_variant['paper'] = photo_variant_model.paper
                        photo_variant['bordered_image'] = photo_variant_model.bordered_image
                        photo_variant['image'] = photo_variant_model.image
                        photo_variant['dpi'] = photo_variant_model.dpi
                        photo_variant['price'] = {'price': photo_variant_model.price}
                        template = {}
                        image_region = {}
                        image_region['top'] = photo_variant_model.image_region_top
                        image_region['width'] = photo_variant_model.image_region_width
                        image_region['left'] = photo_variant_model.image_region_left
                        image_region['height'] = photo_variant_model.image_region_height
                        image_region['angle'] = photo_variant_model.image_region_angle

                        bordered_image_region = {}
                        bordered_image_region['top'] = photo_variant_model.bordered_image_region_top
                        bordered_image_region['width'] = photo_variant_model.bordered_image_region_width
                        bordered_image_region['left'] = photo_variant_model.bordered_image_region_left
                        bordered_image_region['height'] = photo_variant_model.bordered_image_region_height
                        bordered_image_region['angle'] = photo_variant_model.bordered_image_region_angle
                        template['image_region'] = image_region
                        template['bordered_image_region'] = bordered_image_region

                        template['default_frame_orientation'] = photo_variant_model.default_frame_orientation
                        template['is_orientation_switch_allowed'] = photo_variant_model.is_orientation_switch_allowed
                        template['is_colored'] = photo_variant_model.is_colored
                        photo_variant['template'] = template
                        photo_variants.append(photo_variant)
                        tmp_ += 1
                type['variants'] = photo_variants
                item['type'] = type
                items.append(item)
                _ += 1
            for book_model in models.ItemBook.objects.all():
                item = {}
                item['id'] = _
                item['comment'] = book_model.comment

                type = {}
                type['base_variant_id'] = book_model.base_variant_id
                type['base_cover_template_id'] = book_model.base_cover_template_id
                type['base_page_template_id'] = book_model.base_page_template_id
                book_model_page_template_list = [
                    book_model.item_book_page_0,
                    book_model.item_book_page_1,
                    book_model.item_book_page_2,
                    book_model.item_book_page_3,
                    book_model.item_book_page_4,
                    book_model.item_book_page_5,
                    book_model.item_book_page_6,
                    book_model.item_book_page_7,
                    book_model.item_book_page_8,
                    book_model.item_book_page_9,
                ]
                book_model_cover_template_list = [
                    book_model.item_book_cover_0,
                    book_model.item_book_cover_1,
                    book_model.item_book_cover_2,
                    book_model.item_book_cover_3,
                    book_model.item_book_cover_4,
                    book_model.item_book_cover_5,
                    book_model.item_book_cover_6,
                    book_model.item_book_cover_7,
                    book_model.item_book_cover_8,
                    book_model.item_book_cover_9,
                ]
                tmp_ = 0
                page_templates = []
                for book_page_model in book_model_page_template_list:
                    if book_page_model:
                        book_page = {}
                        book_page['id'] = tmp_
                        book_page['image_region'] = {
                            "top": book_page_model.top,
                            "width": book_page_model.width,
                            "left": book_page_model.left,
                            "height": book_page_model.height,
                            "angle": book_page_model.angle,
                        }
                        tmp_ += 1
                        page_templates.append(book_page)
                tmp_ = 0
                page_cover_templates = []
                for book_page_cover_model in book_model_cover_template_list:
                    if book_page_cover_model:
                        book_cover_page = {}
                        book_cover_page['id'] = tmp_
                        book_cover_page['image_region'] = {
                            "top": book_page_cover_model.top,
                            "width": book_page_cover_model.width,
                            "left": book_page_cover_model.left,
                            "height": book_page_cover_model.height,
                            "angle": book_page_cover_model.angle,
                        }
                        tmp_ += 1
                        page_cover_templates.append(book_cover_page)
                variants = [{
                    'id': 0,
                    'paper': book_model.paper,
                    'additional_turn_price': book_model.additional_turn_price,
                    'comment': book_model.comment,
                    'cover_dpi': book_model.cover_dpi,
                    'cover_oms_id': book_model.cover_oms_id,
                    'page_oms_id': book_model.page_oms_id,
                    'page_dpi': book_model.page_dpi,
                    'max_page_count': book_model.max_page_count,
                    'min_page_count': book_model.min_page_count,
                    'uncutted_page_size': {
                        'width': book_model.uncutted_page_size_width,
                        'height': book_model.uncutted_page_size_height,
                    },
                    'cover_size': {
                        'width': book_model.cover_size_width,
                        'height': book_model.cover_size_height,
                    },
                    'uncutted_cover_size': {
                        'width': book_model.uncutted_cover_size_width,
                        'height': book_model.uncutted_cover_size_height,
                    },
                    'cover_turn_size': {
                        'width': book_model.cover_turn_size_width,
                        'height': book_model.cover_turn_size_height,
                    },
                    'uncutted_cover_turn_size': {
                        'width': book_model.uncutted_cover_turn_size_width,
                        'height': book_model.uncutted_cover_turn_size_height,
                    },
                    'page_size': {
                        'width': book_model.page_size_width,
                        'height': book_model.page_size_height,
                    },
                    'price':{
                        'price': book_model.price
                    }
                }]
                type['page_templates'] = page_templates
                type['cover_templates'] = page_cover_templates
                type['variants'] = variants

                item['type'] = type
                items.append(item)
                _ += 1
            response['items'] = items
            response['entries'] = entries
            response['sections'] = sections

        return Response(str(json.dumps(response)), status=status.HTTP_201_CREATED)

