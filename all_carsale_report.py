
from odoo import fields,models,api,_
 class PatientReportWizard(models.TransientModel):
 _name="patient.report.wizard"
 _description="这是一个瞬态模型 patient_report_wizard"
 gender=fields.Selection([(&apos;male&apos;, &apos;;；男&apos;), 
(&apos;female&apos;, &apos;女&apos;), (&apos;other&apos;, &apos;其它
&apos;)],required=True, default=&apos;other&apos;)
 age = fields.Integer(string="Age")
 def action_print_report(self):
 data=
{
 &apos;form_data&apos;:self.read()[0],
 &apos;email&apos;:&apos;6370@163.com&apos;,
 }
return 
self.env.ref(&apos;mysale.action_report_all_patient_details&apos;).report_action(self, 
data=data)
xml 文件代码：【all_carsale_report_view.xml】
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
 <record id="action_report_patient" model="ir.actions.act_window">
 <field name="name">patient_report</field>
 <field name="type">ir.actions.act_window</field>
 <field name="res_model">patient.report.wizard</field>
 <field name="view_mode">form</field>
 <field name="view_id" ref="view_report_patient_form"/>
 <field name="target">new</field>
 </record>
 <record id="view_report_patient_form" model="ir.ui.view">
 <field name="name">patient_report_form</field>
 <field name="model">patient.report.wizard</field>
 <field name="arch" type="xml">
 <form string="创建一个向导">
 <group>
 <group>
 <field name="gender"/>
 </group>
 <group>
 <field name="age"/>
 </group>
 </group>
 <footer>
 <button name="action_print_report" string="打印" 
type="object" class="btn-primary"/>
 <button string="取消" class="btn-secondary" 
special="cancel"/>
 </footer>
 </form>
 </field>
 </record>
 <menuitem id="menu_print_report"
 name="create_print_report"
 parent="menu_1_list"
 action="action_report_patient
py 文件代码：【all_carsale_report.py】
from odoo import api,fields,models
class AllPatientReport(models.AbstractModel):
 _name='report.mysale.report_all_patient_list'
 _description ='patient Report'
 @api.model
 def _get_report_values(self,docids,data=None):
 print("----", docids,data)
 domain=[]
 gender=data.get('form_data').get('gender')
 age=data.get('form_data').get('age')
 if buyer:
 domain+=[('gender','=',gender)]
 if havemoney>=salprice:
 domain+=[('money','=',money)]
 docs=self.env['mysale.mysale'].search(domain)
 return
{
 'docs':docs,
 'email':'admin'
 }
【data 内容】：
---- None {'context': {'lang': 'zh_CN', 'tz': 'Asia/Shanghai', 'uid': 2, 
'allowed_company_ids': [1], 'active_model': 'patient.report.wizard', 
'active_id': 18, 'active_ids': [18]}, 
'form_data': {'id': 18, 'gender': 'other', 'age': 0, '__last_update': '2022-11-13 
16:18:12','display_name': 'patient.report.wizard,18', 'create_uid': [2, 'Administrator'], 
'create_date': '2022-11-13 16:18:12',
'write_uid': [2, 'Administrator'], 'write_date': '2022-11-13 16:18:12'}, 'email': 'admin', 
'report_type': 'pdf'}