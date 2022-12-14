from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import Index, NotesView, TagDeleteView, NoteDeleteView, AddTagView, DetailNoteView, AddNoteView, \
    ChangeNameView, ChangeNoteDescView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('note_book/add_note', AddNoteView.as_view(), name='add_note'),
    path('note_book/', NotesView.as_view(), name='note_book'),
    path('note_book/del_note/<int:pk>', NoteDeleteView.as_view(), name='delete_note'),
    path('note_book/add_tag/<int:note_id>', AddTagView.as_view(), name='add_tag'),
    path('note_book/detail_note/<note_id>', DetailNoteView.as_view(), name='detail_note'),
    path('note_book/change_note/<int:pk>', ChangeNameView.as_view(), name='change_note_name'),
    path('note_book/change_note_description/<int:pk>', ChangeNoteDescView.as_view(), name='change_note_description'),
    path('note_book/detail_note/<int:note_id>/delete_tag/<int:pk>', TagDeleteView.as_view(), name='delete_note_tags'),
]
