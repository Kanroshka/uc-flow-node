from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (Property,
                                  OptionValue, 
                                  DisplayOptions)

from node.schemas.enums import Parameters, Resource, Operation, Api


class NodeType(flow.NodeType):
    id: str = '9a427963-def2-487b-8890-0a0833270c2c'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'example_alfacrm'
    displayName: str = 'Example alfaCRM'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    group: List[str] = ["integration"]
    version: int = 1
    description: str = 'Example alfaCRM'
    inputs: List[str] = ['main']
    outputs: List[str] = ['main']
    credentials: List[flow.NodeType.Credential] = [
        flow.NodeType.Credential(name="alfacrm_api_auth", required=False)
    ]
    properties: List[Property] = [
        Property(
            displayName='API',
            name='api',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='REST API',
                    value=Api.url_api_v2,
                ),
            ],
        ),
        Property(
            displayName='Действие',
            name='resource',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Авторизация',
                    value=Resource.authorization,
                ),
                OptionValue(
                    name='Customer',
                    value=Resource.customer
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        Api.url_api_v2,
                    ],
                },
            ),
        ),
        Property(
            displayName='ALFACRM-TOKEN',
            name='auth_key',
            type=Property.Type.JSON,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.customer, 
                    ],
                    'api': [
                        Api.url_api_v2,
                    ],
                },
            ),
        ),
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Index',
                    value=Operation.get_customers_filtered_and_paging,
                    description='',
                ),
                OptionValue(
                    name='Create',
                    value=Operation.create_customer,
                    description='',
                ),
                OptionValue(
                    name='Update',
                    value=Operation.update_customer,
                    description='',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.customer, 
                    ],
                    'api': [
                        Api.url_api_v2,
                    ],
                },
            ),
        ),
        Property(
            displayName='Branch',
            name='branch',
            type=Property.Type.STRING,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        Api.url_api_v2,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                },
            ),
        ),
        Property(
            displayName='Id customer',
            name='id_customer',
            type=Property.Type.STRING,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        Api.url_api_v2,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.update_customer,
                    ],
                },
            ),
        ),
        Property(
            displayName='Return all',
            name='return_all',
            type=Property.Type.BOOLEAN,
            default=True,
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        Api.url_api_v2,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.get_customers_filtered_and_paging,
                    ],
                },
            ),
        ),
        Property(
            displayName='Page',
            name='page',
            type=Property.Type.NUMBER,
            default=1,
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        Api.url_api_v2,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.get_customers_filtered_and_paging,
                    ],
                    'return_all': [
                        False,
                    ],
                },
            ),
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            default={},
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        Api.url_api_v2,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.get_customers_filtered_and_paging,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='id',
                    name=Parameters.customer_id,
                    description='id клиента',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            name=Parameters.customer_id,
                            default='',
                        ),
                    ],
                ),
                Property(
                    displayName='is study',
                    description='состояние клиента (0-лид, 1-клиент)',
                    noDataExpression=True,
                    name=Parameters.customer_is_study,
                    values=[
                        Property(
                            name=Parameters.customer_is_study,
                            type=Property.Type.OPTIONS,
                            options=[
                                OptionValue(
                                    name='Клиент',
                                    value=1,
                                ),
                                OptionValue(
                                    name='Лид',
                                    value=0,
                                )
                            ],
                            default='',
                        ),
                    ],
                ),
                Property(
                    displayName='study_status_id',
                    name=Parameters.customer_study_status_id,
                    description='id статуса клиента',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            name=Parameters.customer_study_status_id,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='name',
                    name=Parameters.customer_name,
                    description='имя клиента',
                    values=[
                        Property(
                            name=Parameters.customer_name,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='gender',
                    name=Parameters.customer_gender,
                    description='пол клиента',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            name=Parameters.customer_gender,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='age_from',
                    name=Parameters.customer_age_from,
                    description='возраст клиента от',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            name=Parameters.customer_age_from,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='age_to',
                    name=Parameters.customer_age_to,
                    description='возраст клиента до',
                    values=[
                        Property(
                            name=Parameters.customer_age_to,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='phone',
                    name=Parameters.customer_phone,
                    description='контакты клиента',
                    values=[
                        Property(
                            name=Parameters.customer_phone,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='legal_type',
                    name=Parameters.customer_legal_type,
                    description='тип заказчика(1-физ лицо, 2-юр.лицо)',
                    values=[
                        Property(
                            type=Property.Type.OPTIONS,
                            name=Parameters.customer_legal_type,
                            default='',
                            options=[
                                OptionValue(
                                    name='Физ. лицо',
                                    value=1
                                ),
                                OptionValue(
                                    name='Юр. лицо',
                                    value=2,
                                ),
                            ],
                        ),
                    ],
                ),
                Property(
                    displayName='legal_name',
                    name=Parameters.customer_legal_name,
                    description='имя заказчика',
                    values=[
                        Property(
                            name=Parameters.customer_legal_name,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='company_id',
                    name=Parameters.customer_company_id,
                    description='id юр лица',
                    values=[
                        Property(
                            name=Parameters.customer_company_id,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='lesson_count_from',
                    name=Parameters.customer_lesson_count_from,
                    description='остаток уроков от',
                    values=[
                        Property(
                            name=Parameters.customer_lesson_count_from,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='lesson_count_to',
                    name=Parameters.customer_lesson_count_to,
                    description='остаток уроков до',
                    values=[
                        Property(
                            name=Parameters.customer_lesson_count_to,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='balance_contract_from',
                    name=Parameters.customer_balance_contract_from,
                    description='баланс договора от',
                    values=[
                        Property(
                            name=Parameters.customer_balance_contract_from,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='balance_contract_to',
                    name=Parameters.customer_balance_contract_to,
                    description='баланс договора до',
                    values=[
                        Property(
                            name=Parameters.customer_balance_contract_to,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='balance_bonus_from',
                    name=Parameters.customer_balance_bonus_from,
                    description='баланс бонусов от',
                    values=[
                        Property(
                            name=Parameters.customer_balance_bonus_from,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='balance_bonus_to',
                    name=Parameters.customer_balance_bonus_from,
                    description='баланс бонусов до',
                    values=[
                        Property(
                            name=Parameters.customer_balance_bonus_from,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='removed',
                    name=Parameters.customer_removed,
                    description='флаг архивности (2 - только архивные, 1 - активные и архивные, 0 – только активные)',
                    values=[
                        Property(
                            type=Property.Type.OPTIONS,
                            name=Parameters.customer_removed,
                            default='',
                            options=[
                                OptionValue(
                                    name='Только архивные',
                                    value=2,
                                ),
                                OptionValue(
                                    name='Активные и архивные',
                                    value=1,
                                ),
                                OptionValue(
                                    name='Только активные',
                                    value=0,
                                ),
                            ],
                        ),
                    ],
                ),
                Property(
                    displayName='removed_from',
                    name=Parameters.customer_removed_from,
                    description='дата отправки в архив от',
                    values=[
                        Property(
                            name=Parameters.customer_removed_from,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='removed_to',
                    name=Parameters.customer_removed_to,
                    description='дата отправки в архив',
                    values=[
                        Property(
                            name=Parameters.customer_removed_to,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='level_id',
                    name=Parameters.customer_level_id,
                    description='id уровня знаний',
                    values=[
                        Property(
                            name=Parameters.customer_level_id,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='assigned_id',
                    name=Parameters.customer_assigned_id,
                    description='id ответственного менеджера',
                    values=[
                        Property(
                            name=Parameters.customer_assigned_id,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='employee_id',
                    name=Parameters.customer_employee_id,
                    description='id ответственного педагога',
                    values=[
                        Property(
                            name=Parameters.customer_employee_id,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='lead_source_id',
                    name=Parameters.customer_lead_source_id,
                    description='id источника',
                    values=[
                        Property(
                            name=Parameters.customer_lead_source_id,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='color',
                    name=Parameters.customer_color,
                    description='id цвета',
                    values=[
                        Property(
                            name=Parameters.customer_color,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='note',
                    name=Parameters.customer_note,
                    description='примечание',
                    values=[
                        Property(
                            name=Parameters.customer_note,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='date_from',
                    name=Parameters.customer_date_from,
                    description='дата добавления от',
                    values=[
                        Property(
                            name=Parameters.customer_date_from,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='date_to',
                    name=Parameters.customer_date_to,
                    description='дата добавления до',
                    values=[
                        Property(
                            name=Parameters.customer_date_to,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='next_lesson_date_from',
                    name=Parameters.customer_next_lesson_date_from,
                    description='дата след.посещения от',
                    values=[
                        Property(
                            name=Parameters.customer_next_lesson_date_from,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='next_lesson_date_to',
                    name=Parameters.customer_next_lesson_date_to,
                    description='дата след.посещения до',
                    values=[
                        Property(
                            name=Parameters.customer_next_lesson_date_to,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='tariff_till_from',
                    name=Parameters.customer_tariff_till_from,
                    description='дата действия абонемента от',
                    values=[
                        Property(
                            name=Parameters.customer_tariff_till_from,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='tariff_till_to',
                    name=Parameters.customer_tariff_till_to,
                    description='дата действия абонемента до',
                    values=[
                        Property(
                            name=Parameters.customer_tariff_till_to,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='customer_reject_id',
                    name=Parameters.customer_reject_id,
                    description='id причины отказа',
                    values=[
                        Property(
                            name=Parameters.customer_reject_id,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='comment',
                    name=Parameters.customer_comment,
                    description='комментарий',
                    values=[
                        Property(
                            name=Parameters.customer_comment,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='dob_from',
                    name=Parameters.customer_dob_from,
                    description='дата рождения от',
                    values=[
                        Property(
                            name=Parameters.customer_dob_from,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='dob_to',
                    name=Parameters.customer_dob_to,
                    description='дата рождения до',
                    values=[
                        Property(
                            name=Parameters.customer_dob_to,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='withGroups:true',
                    name=Parameters.customer_with_groups_true,
                    description='активные группы клиента',
                    values=[
                        Property(
                            name=Parameters.customer_with_groups_true,
                            type=Property.Type.STRING,
                            default='',
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            default={},
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        Api.url_api_v2,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.create_customer,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='name',
                    name=Parameters.customer_name,
                    description='имя клиента',
                    values=[
                        Property(
                            name=Parameters.customer_name,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='is study',
                    name=Parameters.customer_is_study,
                    description='состояние клиента (0-лид, 1-клиент)',
                    noDataExpression=True,
                    values=[
                        Property(
                            name=Parameters.customer_is_study,
                            type=Property.Type.OPTIONS,
                            options=[
                                OptionValue(
                                    name='Клиент',
                                    value=1,
                                    type=Property.Type.NUMBER,
                                ),
                                OptionValue(
                                    name='Лид',
                                    value=0,
                                    type=Property.Type.NUMBER,
                                )
                            ],
                            default='',
                        ),
                    ],
                ),
                Property(
                    displayName='legal_type',
                    name=Parameters.customer_legal_type,
                    description='тип заказчика(1-физ лицо, 2-юр.лицо)',
                    values=[
                        Property(
                            type=Property.Type.OPTIONS,
                            name=Parameters.customer_legal_type,
                            default='',
                            options=[
                                OptionValue(
                                    name='Физ. лицо',
                                    value=1,
                                    type=Property.Type.NUMBER,
                                ),
                                OptionValue(
                                    name='Юр. лицо',
                                    value=2,
                                    type=Property.Type.NUMBER,
                                ),
                            ],
                        ),
                    ],
                    
                ),
                Property(
                    displayName='branch_ids',
                    name=Parameters.customer_branch_ids,
                    description='массив идентификаторов филиалов',
                    values=[
                        Property(
                            name=Parameters.customer_branch_ids,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ]
                ),
            ]
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            default={},
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        Api.url_api_v2,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.update_customer,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='name',
                    name=Parameters.customer_name,
                    description='имя клиента',
                    values=[
                        Property(
                            name=Parameters.customer_name,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='is study',
                    name=Parameters.customer_is_study,
                    description='состояние клиента (0-лид, 1-клиент)',
                    noDataExpression=True,
                    values=[
                        Property(
                            name=Parameters.customer_is_study,
                            type=Property.Type.OPTIONS,
                            options=[
                                OptionValue(
                                    name='Клиент',
                                    value=1,
                                    type=Property.Type.NUMBER,
                                ),
                                OptionValue(
                                    name='Лид',
                                    value=0,
                                    type=Property.Type.NUMBER,
                                )
                            ],
                            default='',
                        ),
                    ],
                ),
                Property(
                    displayName='legal_type',
                    name=Parameters.customer_legal_type,
                    description='тип заказчика(1-физ лицо, 2-юр.лицо)',
                    values=[
                        Property(
                            type=Property.Type.OPTIONS,
                            name=Parameters.customer_legal_type,
                            default='',
                            options=[
                                OptionValue(
                                    name='Физ. лицо',
                                    value=1,
                                    type=Property.Type.NUMBER,
                                ),
                                OptionValue(
                                    name='Юр. лицо',
                                    value=2,
                                    type=Property.Type.NUMBER,
                                ),
                            ],
                        ),
                    ],   
                ),
                 Property(
                    displayName='phone',
                    name=Parameters.customer_phone,
                    description='контакты клиента',
                    values=[
                        Property(
                            name=Parameters.customer_phone,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='gender',
                    name=Parameters.customer_gender,
                    description='пол клиента',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            name=Parameters.customer_gender,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='company_id',
                    name=Parameters.customer_company_id,
                    description='id юр лица',
                    values=[
                        Property(
                            name=Parameters.customer_company_id,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='dob_from',
                    name=Parameters.customer_dob_from,
                    description='дата рождения от',
                    values=[
                        Property(
                            name=Parameters.customer_dob_from,
                            type=Property.Type.DATE,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='balance_contract_from',
                    name=Parameters.customer_balance_contract_from,
                    description='баланс договора от',
                    values=[
                        Property(
                            name=Parameters.customer_balance_contract_from,
                            type=Property.Type.NUMBER,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='email',
                    name=Parameters.customer_email,
                    description='email',
                    values=[
                        Property(
                            name=Parameters.customer_email,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='web',
                    name=Parameters.customer_web,
                    description='web',
                    values=[
                        Property(
                            name=Parameters.customer_web,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
                Property(
                    displayName='legal_name',
                    name=Parameters.customer_legal_name,
                    description='имя заказчика',
                    values=[
                        Property(
                            name=Parameters.customer_legal_name,
                            type=Property.Type.STRING,
                            default='',
                        )
                    ],
                ),
            ],
        ),
    ]
