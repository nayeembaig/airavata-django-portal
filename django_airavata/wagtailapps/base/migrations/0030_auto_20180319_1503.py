# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-19 15:03
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('django_airavata_wagtail_base', '0029_auto_20180319_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='list-ul', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.RichTextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html'))), blank=True, null=True, verbose_name='About content block'),
        ),
        migrations.AlterField(
            model_name='blankpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='list-ul', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.RichTextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html'))), verbose_name='Blank content block'),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='list-ul', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.RichTextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html'))), blank=True, null=True, verbose_name='Contact content block'),
        ),
        migrations.AlterField(
            model_name='documentationpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='list-ul', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.RichTextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html'))), blank=True, null=True, verbose_name='Documentation content block'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='list-ul', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.RichTextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html'))), blank=True, null=True, verbose_name='Home content block'),
        ),
    ]
