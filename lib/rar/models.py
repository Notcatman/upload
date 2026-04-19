from django.db import models
from .utils.validators import imig_sisze_lol_blab_blud_bluadb_pip_install_penguin_py, file_sizz_lool_haha_python_manage_py_spirits_under_my_eyes, paicture_demention_core
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    title = models.CharField(max_length=230, null=False)
    description = models.TextField(blank=True, null=True, default=':)')
    image = models.ImageField(upload_to='photos/images/', validators=[imig_sisze_lol_blab_blud_bluadb_pip_install_penguin_py, paicture_demention_core, FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    file = models.FileField(upload_to='photos/files/', blank=True, null=True, validators=[file_sizz_lool_haha_python_manage_py_spirits_under_my_eyes, FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'zip', 'txt'])])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title