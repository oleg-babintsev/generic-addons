# -*- coding: utf-8 -*-

from openerp.tests import common


class BaseActionRuleTest(common.TransactionCase):

    def setUp(self):
        """*****setUp*****"""
        super(BaseActionRuleTest, self).setUp()

        self.test_model = self.env.ref('generic_tag_test.test_tag_model')
        self.test_record_1 = self.env.ref('generic_tag_test.taggable_object_1')
        self.test_record_2 = self.env.ref('generic_tag_test.taggable_object_2')
        self.test_tag_cat_1 = self.env.ref(
            'generic_tag_test.test_tag_category_1')
        self.test_tag_1 = self.env.ref('generic_tag_test.test_tag_1')
        self.test_tag_2 = self.env.ref('generic_tag_test.test_tag_2')
        self.test_tag_3 = self.env.ref('generic_tag_test.test_tag_3')

        self.env['base.action.rule']._register_hook()

    def test_20_test_rule_actions(self):
        """ Test that rule_actions work fine
        """
        self.assertEquals(len(self.test_record_1.tag_ids), 0)

        # Test that act_add_field works fine
        self.test_record_1.write({'test_field': 'add'})
        self.assertEquals(self.test_record_1.test_field, 'add')
        self.assertEquals(len(self.test_record_1.tag_ids), 1)
        self.assertEquals(self.test_record_1.tag_ids[0].name, 'TC1')

        # Add another tag to object
        self.test_record_1.add_tag(name='TC2')
        self.assertEquals(len(self.test_record_1.tag_ids), 2)

        # Test that act_rem_field works fine
        self.test_record_1.write({'test_field': 'remove'})
        self.assertEquals(self.test_record_1.test_field, 'remove')
        self.assertEquals(len(self.test_record_1.tag_ids), 1)
        self.assertEquals(self.test_record_1.tag_ids[0].name, 'TC2')