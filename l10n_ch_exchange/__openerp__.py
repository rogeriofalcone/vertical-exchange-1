# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Yannick Buron, Lucas Huber
#    Copyright 2015 Yannick Buron
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Wallet Swiss localization',
    'version': '1.0',
    'category': 'Accounting',
    'author': 'Lucas Huber',
    'license': 'AGPL-3',
    'description': """
Wallet Swiss localization
==========================

Add accounts to manage wallet inside Swiss chart account
---------------------------------------------------------
""",
    'website': 'https://github.com/jeema-solutions/vertical-community',
    'depends': [
        'exchange',
        'l10n_ch',
    ],
    'data': ['l10n_ch_wallet_account_data.xml'],
    'installable': True,
}
