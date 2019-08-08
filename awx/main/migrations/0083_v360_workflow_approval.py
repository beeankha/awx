# Generated by Django 2.2.4 on 2019-08-02 17:51

import awx.main.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0082_v360_webhook_http_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowApprovalTemplate',
            fields=[
                ('unifiedjobtemplate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.UnifiedJobTemplate')),
                ('timeout', models.IntegerField(blank=True, default=0, help_text='The amount of time (in seconds) before the approval node expires and fails.')),
            ],
            bases=('main.unifiedjobtemplate',),
        ),
        migrations.AddField(
            model_name='organization',
            name='approval_role',
            field=awx.main.fields.ImplicitRoleField(editable=False, null='True', on_delete=django.db.models.deletion.CASCADE, parent_role='admin_role', related_name='+', to='main.Role'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='workflowjobtemplate',
            name='approval_role',
            field=awx.main.fields.ImplicitRoleField(editable=False, null='True', on_delete=django.db.models.deletion.CASCADE, parent_role=['organization.approval_role', 'admin_role'], related_name='+', to='main.Role'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='workflowjobnode',
            name='unified_job_template',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflowjobnodes', to='main.UnifiedJobTemplate'),
        ),
        migrations.AlterField(
            model_name='workflowjobtemplatenode',
            name='unified_job_template',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflowjobtemplatenodes', to='main.UnifiedJobTemplate'),
        ),
        migrations.CreateModel(
            name='WorkflowApproval',
            fields=[
                ('unifiedjob_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.UnifiedJob')),
                ('workflow_approval_template', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approvals', to='main.WorkflowApprovalTemplate')),
            ],
            bases=('main.unifiedjob',),
        ),
        migrations.AddField(
            model_name='activitystream',
            name='workflow_approval',
            field=models.ManyToManyField(blank=True, to='main.WorkflowApproval'),
        ),
        migrations.AddField(
            model_name='activitystream',
            name='workflow_approval_template',
            field=models.ManyToManyField(blank=True, to='main.WorkflowApprovalTemplate'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='read_role',
            field=awx.main.fields.ImplicitRoleField(editable=False, null='True', on_delete=django.db.models.deletion.CASCADE, parent_role=['member_role', 'auditor_role', 'execute_role', 'project_admin_role', 'inventory_admin_role', 'workflow_admin_role', 'notification_admin_role', 'credential_admin_role', 'job_template_admin_role', 'approval_role'], related_name='+', to='main.Role'),
        ),
        migrations.AlterField(
            model_name='workflowjobtemplate',
            name='read_role',
            field=awx.main.fields.ImplicitRoleField(editable=False, null='True', on_delete=django.db.models.deletion.CASCADE, parent_role=['singleton:system_auditor', 'organization.auditor_role', 'execute_role', 'admin_role', 'approval_role'], related_name='+', to='main.Role'),
        ),
        migrations.AddField(
            model_name='workflowapproval',
            name='timeout',
            field=models.IntegerField(blank=True, default=0, help_text='The amount of time (in seconds) before the approval node expires and fails.'),
        ),
        migrations.AddField(
            model_name='workflowapproval',
            name='timed_out',
            field=models.BooleanField(default=False, help_text='Shows when an approval node (with a timeout assigned to it) has timed out.'),
        ),
    ]
