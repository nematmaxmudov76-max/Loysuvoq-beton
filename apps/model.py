from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Yaratilgan vaqti"
    )  # model yaratishda avtomatik ravishda hozirgi vaqtni saqlaydi
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="O'zgartirilgan vaqti"
    )  # model saqlanayotganda avtomatik ravishda hozirgi vaqtni saqlaydi

    class Meta:
        abstract = True
