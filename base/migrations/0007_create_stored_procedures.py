from django.db import migrations

def load_sql_file(apps, schema_editor):
    with open('base/init.sql', 'r') as f:
        sql = f.read()
    schema_editor.execute(sql)

class Migration(migrations.Migration):
    dependencies = [
        # Add your migration dependencies here
        ('base', '0006_loan'),
    ]

    operations = [
        migrations.RunPython(load_sql_file),
    ]
