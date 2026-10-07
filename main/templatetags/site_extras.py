from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def wobble_last_word(value):
    """Wrap the last word's letters in spans (for the CSS wobble animation), keep the rest as plain text."""
    if not value:
        return ""
    words = value.strip().split(" ")
    *head, last = words
    letters_html = "".join(f"<span>{escape(ch)}</span>" for ch in last)
    prefix = escape(" ".join(head) + " ") if head else ""
    return mark_safe(f'{prefix}<span class="wobble-word">{letters_html}</span>')
