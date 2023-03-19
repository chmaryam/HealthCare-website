# Generated by Django 4.1.7 on 2023-03-18 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brief', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='main_app/static/images/department')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_role', models.CharField(max_length=100)),
                ('mobile_Number', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='main_app/static/images/users')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_contact', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('blood', models.CharField(max_length=100)),
                ('cpr', models.CharField(max_length=100)),
                ('height', models.FloatField(max_length=5)),
                ('weight', models.FloatField(max_length=5)),
                ('dof', models.DateField(max_length=100)),
                ('sensitivity', models.TextField(max_length=5000)),
                ('profile', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('shift', models.CharField(choices=[('1', 'Early Morning'), ('2', 'Late Morning'), ('3', 'Evening')], default='1', max_length=1)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile_contact', serialize=False, to='main_app.profile')),
                ('description', models.TextField(max_length=5000)),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.patient')),
            ],
        ),
    ]