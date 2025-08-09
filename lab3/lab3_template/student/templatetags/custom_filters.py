from django import template

register = template.Library()

@register.filter
def double(value):
    """يرجع القيمة مضروبة في 2"""
    return value * 2

@register.filter
def format_riyals(value):
    """تحويل الرقم إلى عملة ريال سعودي"""
    return f"{value:,} ريال"

@register.filter
def age_label(value):
    """تحديد تصنيف العمري"""
    if value < 18:
        return "قاصر"
    elif 18 <= value <= 60:
        return "بالغ"
    else:
        return "كبير سن"
