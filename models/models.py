# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api

class vetapp_animal(models.Model):
    _name = 'vetapp.animal'
    _description ="Animal Model"
    @api.one
    def _compute_age(self):
        if self.birthdate:
            self.age = (fields.date.today() - self.birthdate) / timedelta(365.2425)

    name = fields.Char('Name', required=True)
    species_id = fields.Many2one('vetapp.species', required=True)
    breed_id = fields.Many2one('vetapp.breed', domain="[('species_id' ,'=', species_id)]", required=True)
    owner_id = fields.Many2one('res.partner', domain="[('customer','=',True)]", required=True)
    ownerphone = fields.Char(related='owner_id.phone', store=True)
    diagnosis_ids = fields.Many2many('vetapp.diagnosis')
    age = fields.Float(compute=_compute_age)
    birthdate = fields.Date('Date of Birth', help="If you dont know the exact Birthdate, enter the best guess")
    spayorneuter = fields.Boolean('Spayed or Neutered')
    notes = fields.Text('Notes', default="This is where you need to put notes...")
    firstvisit = fields.Datetime('First Visit', default=lambda self: fields.Datetime.now())
    image_medium = fields.Binary('Medium-size image', attachment=True)

class vetapp_species(models.Model):
    _name = 'vetapp.species'
    _description = "Species Model"
    name = fields.Char('Species Name')
    animal_ids = fields.One2many('vetapp.animal', 'owner_id', 'Animal List')
    notes = fields.Text()

class vetapp_breed(models.Model):
    _name = 'vetapp.breed'
    _description = "Breed Model"
    name = fields.Char('Breed Name')
    species_id = fields.Many2one('vetapp.species')
    animal_ids = fields.One2many('vetapp.animal', 'owner_id', 'Animal List')
    notes = fields.Text()

class vetapp_partner(models.Model):
    _inherit = 'res.partner'
    animal_ids = fields.One2many('vetapp.animal', 'owner_id', 'Animal List')
    orientation_complited = fields.Boolean('Orientation Complited')
    orientation_staff_id = fields.Many2one('res.users')

class vetapp_diagnosis(models.Model):
    _name = 'vetapp.diagnosis'
    _description = 'Diagnosis Model'
    name = fields.Char('Diagnosis')
    code = fields.Char('Diagnostic code')
    symptoms_ids = fields.Many2many('vetapp.symptoms')
    treatment_ids = fields.Many2many('vetapp.treatment')
    notes = fields.Text()

class vetapp_symptoms(models.Model):
    _name = 'vetapp.symptoms'
    _description = 'Symptoms Model'
    name = fields.Char('symptoms')
    code = fields.Char('symptoms code')
    diagnosis_ids = fields.Many2many('vetapp.diagnosis')
    notes = fields.Text()

class vetapp_treatment(models.Model):
    _name = 'vetapp.treatment'
    _description = 'Treatment Model'
    name = fields.Char('treatment')
    code = fields.Char('treatment code')
    diagnosis_ids = fields.Many2many('vetapp.diagnosis')
    product_ids = fields.Many2many('product.template')
    notes = fields.Text()

class vetapp_product(models.Model):
    _inherit = 'product.template'
    treatment_ids = fields.Many2many('vetapp.treatment')