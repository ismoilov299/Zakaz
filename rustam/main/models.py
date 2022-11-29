from django.db import models


class Setting(models.Model):
	copyright = models.CharField('Copyright', max_length=100, default='')
	token = models.CharField('Телеграм токен', max_length=100, default='')
	tag = models.CharField('Телеграм тэг', max_length=100, default='')

	def __str__(self):
		return 'Настройки'

	def get_settings():
		settings = Setting.objects.filter(id=1)
		if settings:
			return settings[0]
		else:
			settings = Setting()
			settings.save()
			return settings

	def telegram_url(self):
		if '@' in self.tag:
			self.tag = self.tag.replace('@', '')
			return 'https://t.me/' + self.tag
