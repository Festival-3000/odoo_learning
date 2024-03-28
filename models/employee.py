from datetime import datetime,timedelta
from odoo import fields, models, api

class EmployeesDetail(models.Model):
    _name = 'employees.name'
    _description = 'Employees Name'

    emp_name = fields.Char(default="Employee",string="Employee Name")
    emp_email = fields.Text(default="employee@gmail.com",string="Employee Email")
    emp_address = fields.Text(default="Gandhinagar",string="Employee Address")
    emp_contact_no = fields.Text(default="+911234567890",string="Employee Contact Details")
    emp_age = fields.Integer(default="21",string="Employee Age")
    emp_gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],string="Employee Gender",default="Male")
    emp_date_of_birth = fields.Date(string="Employee Date of Birth")
    emp_salary = fields.Float(string="Employee Salary")
    emp_is_active = fields.Boolean(default="True",string="Is Employee Active")
    emp_html = fields.Html(string="Employee Website")
    emp_image = fields.Binary(string="Employee Image")
    created_date = fields.Datetime(string="Created Date",default=fields.Datetime.now,readonly=True)


class ClientsDetails(models.Model):
    _name = 'clients.name'
    _description = 'Clients Name'

    client_name = fields.Char(default="Client", string="Client Name")
    client_email = fields.Text(default="client@gmail.com",string="Client Email")
    client_address = fields.Text(default="Ahemdabad",string="Client Address")
    client_contact_no = fields.Text(default="+919876543210",string="Client Contact Details")
    client_age = fields.Integer(default="21",string="Client Age")
    client_gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],string="Client Gender")
    client_date_of_birth = fields.Date(string="Client Date of Birth")
    client_amount = fields.Float(string="Client Amount")
    client_is_active = fields.Boolean(default="True",string="Is Client Active")
    client_html = fields.Html(string="Client Website")
    client_image = fields.Binary(string="Client Image")
    created_date = fields.Datetime(string="Created Date",default=fields.Datetime.now,readonly=True)


class ProjectsDetails(models.Model):
    _name = 'projects.name'
    _description = 'Projects Name'

    project_name = fields.Char(default="Enter Project Name", string="Project Name")
    project_image = fields.Binary(string="Project Image")
    project_desc = fields.Text(default="Enter Project Description",string="Project Description")
    project_state = fields.Selection([('to do','To Do'),('in_progress','In Progress'),('done','Done')],string="Status",default="to do")
    start_date = fields.Date(string="Start Date",default=lambda self: (datetime.today()))
    deadline_date = fields.Date(string="Deadline Date",default=lambda self: (datetime.today() + timedelta(days=30)))
    created_date = fields.Datetime(string="Created Date",default=fields.Datetime.now,readonly=True)
    date_diff = fields.Integer(string="Date Difference", compute = '_compute_date_diff')
    date_left = fields.Integer(string="Days Left", compute = '_compute_days_left')

    @api.depends('start_date','deadline_date')
    def _compute_date_diff(self):
        for record in self:
            if record.start_date and record.deadline_date:
                diff = (record.deadline_date - record.start_date).days
                record.date_diff = diff
            else:
                record.date_diff = 0

    @api.depends('deadline_date')
    def _compute_days_left(self):
        today_date = datetime.today()
        for record in self:
            if record.deadline_date:
                remaining_days = (record.deadline_date - today_date).days
                record.date_left = remaining_days if remaining_days >=0 else 0
            else:
                record.date_left = 0