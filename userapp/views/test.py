import ast

a = {
    "analysis_type": "0",
    "property_details": {
        "asset_name": "",
        "asset_address": "",
        "original_purchase_price": "",
        "no_years": "10",
        "total_sft": "",
        "no_units": "1",
        "asset_appraisal_value": "5",
        "asset_appraisal_type": "0",
        "sales_expense_value": "5",
        "sales_expense_type": "0",
        "ammortization_years": "30",
        "acquired_on": "",
        "annual_rate_interests": "",
        "annual_rate_interests_type": "0",
    },
    "loan_details": {
        "amount_down_payment_value": "25",
        "amount_down_payment_type": "0",
        "amount_down_payment": "0",
        "mortgage_loan": "0",
        "gross_income": "",
        "noi": "",
        "cap_rate": "",
        "year1_roi": "0",
        "total_roi_percentage": "0",
        "total_roi": "0",
    },
    "closing_detials": {
        "closing_consession": [
            {
                "closing_consessions_view": "0",
                "closing_consession_name": "Closing Concession",
                "closing_consessionamount": "0",
            }
        ],
        "closing_expense": [
            {
                "closing_expenses_view": "0",
                "closing_expensename": "Closing Expenses",
                "closing_expenseamount": "0",
            }
        ],
    },
    "tenant_details": [
        {
            "tenant_name": "Tenant1",
            "sft_leased": "8",
            "lease_rate": "",
            "lease_rate_type": "0",
            "rent_frequency": "0",
            "frequency_data": [
                {
                    "rent_increase_value": "0",
                    "rent_increases": "0",
                    "rent_increases_for_every_year": "1",
                }
            ],
        },
        {
            "tenant_name": "",
            "sft_leased": "",
            "lease_rate": "",
            "lease_rate_type": "0",
            "rent_frequency": "0",
            "frequency_data": [
                {
                    "" "rent_increase_value": "0",
                    "rent_increases": "0",
                    "rent_increases_for_every_year": "1",
                }
            ],
        },
        {
            "tenant_name": "",
            "sft_leased": "",
            "lease_rate": "",
            "lease_rate_type": "0",
            "rent_frequency": "0",
            "frequency_data": [
                {
                    "rent_increase_value": "0",
                    "rent_increases": "0",
                    "rent_increases_for_every_year": "1",
                }
            ],
        },
    ],
    "additional_income_details": [
        {
            "income_name": "",
            "income_amount": "",
            "income_frequency": "0",
            "frequency_data": [
                {
                    "income_increase_value": "0",
                    "income_increases_type": "0",
                    "income_increases_for_every_year": "1",
                },
                {
                    "income_increase_value": "0",
                    "income_increases_type": "0",
                    "income_increases_for_every_year": "1",
                },
            ],
        }
    ],
    "expenses_details": {
        "taxes": {
            "expense_taxes": "0",
            "taxes_ye_mo": "0",
            "taxes_frequency": "0",
            "taxes_increase_value": ["0"],
            "taxes_increases_type": ["0"],
            "taxes_increases_for_every_year": ["1"],
        },
        "insurance": {
            "insurance_expense": "0",
            "insu_ye_mo": "0",
            "insu_frequency": "0",
            "insu_increase_value": ["0"],
            "insu_increases_type": ["0"],
            "insu_increases_for_every_year": ["1"],
        },
        "hoa": {
            "expense_hoa": "0",
            "hoa_ye_mo": "0",
            "hoa_frequency": "0",
            "hoa_increase_value": ["0"],
            "hoa_increases_type": ["0"],
            "hoa_increases_for_every_year": ["1"],
        },
    },
    "other_expenses": {
        "expense_maintenance": "3",
        "expense_maintenance_type": "0",
        "expense_vacancy": "4",
        "expense_vacancy_type": "0",
        "property_mgmt": "6",
        "property_mgmt_type": "0",
    },
    "additional_expenses": [
        {
            "expense_head_name": "",
            "expense_amount": "",
            "expense_frequency": "0",
            "frequency_data": [
                {
                    "expense_increase_value": "0",
                    "expense_increases_type": "0",
                    "expense_increases_for_every_year": "1",
                }
            ],
        },
    ],
}

d = {}
print(a)
for k, v in a.items():
    if k == "analysis_type":
        d["analysis_type"] = ast.literal_eval('["' + a[k] + '"]')
    elif k == "property_details":
        for ik, iv in v.items():
            d[ik] = ast.literal_eval('["' + iv + '"]')

    elif k == "loan_details":
        for ik, iv in v.items():
            d[ik] = ast.literal_eval('["' + iv + '"]')

    elif k == "closing_detials":
        for ik, iv in v.items():
            if ik == "closing_consession":
                for x in iv:
                    d["closing_consessions_view"] = ast.literal_eval(
                        '["' + x["closing_consessions_view"] + '"]'
                    )
                    d["closing_consession_name"] = ast.literal_eval(
                        '["' + x["closing_consession_name"] + '"]'
                    )
                    d["closing_consessionamount"] = ast.literal_eval(
                        '["' + x["closing_consessionamount"] + '"]'
                    )
            if ik == "closing_expense":
                for x in iv:
                    d["closing_expenses_view"] = ast.literal_eval(
                        '["' + x["closing_expenses_view"] + '"]'
                    )
                    d["closing_expensename"] = ast.literal_eval(
                        '["' + x["closing_expensename"] + '"]'
                    )
                    d["closing_expenseamount"] = ast.literal_eval(
                        '["' + x["closing_expenseamount"] + '"]'
                    )

    elif k == "tenant_details":
        d["tenant_nums"] = ""
        for index, x in enumerate(v):
            if index != len(v) - 1:
                d["tenant_nums"] = d["tenant_nums"] + str(index) + ","
            else:
                d["tenant_nums"] = d["tenant_nums"] + str(index)
            for ik, iv in x.items():
                if ik == "frequency_data":
                    for x in iv:
                        if d.get("rent_increase_value" + "[" + str(index) + "]"):
                            d["rent_increase_value" + "[" + str(index) + "]"].append(
                                x["rent_increase_value"]
                            )
                            d["rent_increases" + "[" + str(index) + "]"].append(
                                x["rent_increases"]
                            )
                            d[
                                "rent_increases_for_every_year" + "[" + str(index) + "]"
                            ].append(x["rent_increases_for_every_year"])
                        else:
                            d[
                                "rent_increase_value" + "[" + str(index) + "]"
                            ] = ast.literal_eval('["' + x["rent_increase_value"] + '"]')
                            d[
                                "rent_increases" + "[" + str(index) + "]"
                            ] = ast.literal_eval('["' + x["rent_increases"] + '"]')
                            d[
                                "rent_increases_for_every_year" + "[" + str(index) + "]"
                            ] = ast.literal_eval(
                                '["' + x["rent_increases_for_every_year"] + '"]'
                            )
                else:
                    if d.get(ik):
                        d[ik].append(iv)
                    else:
                        d[ik] = ast.literal_eval('["' + iv + '"]')

        d["tenant_nums"] = ast.literal_eval('["' + d["tenant_nums"] + '"]')

    elif k == "additional_income_details":
        d["additional_income_nums"] = ""
        for index, x in enumerate(v):
            if index != len(v) - 1:
                d["additional_income_nums"] = (
                    d["additional_income_nums"] + str(index) + ","
                )
            else:
                d["additional_income_nums"] = d["additional_income_nums"] + str(index)
            for ik, iv in x.items():
                if ik == "frequency_data":
                    for x in iv:
                        if d.get("income_increase_value" + "[" + str(index) + "]"):
                            d["income_increase_value" + "[" + str(index) + "]"].append(
                                x["income_increase_value"]
                            )
                            d["income_increases_type" + "[" + str(index) + "]"].append(
                                x["income_increases_type"]
                            )
                            d[
                                "income_increases_for_every_year"
                                + "["
                                + str(index)
                                + "]"
                            ].append(x["income_increases_for_every_year"])
                        else:
                            d[
                                "income_increase_value" + "[" + str(index) + "]"
                            ] = ast.literal_eval(
                                '["' + x["income_increase_value"] + '"]'
                            )
                            d[
                                "income_increases_type" + "[" + str(index) + "]"
                            ] = ast.literal_eval(
                                '["' + x["income_increases_type"] + '"]'
                            )
                            d[
                                "income_increases_for_every_year"
                                + "["
                                + str(index)
                                + "]"
                            ] = ast.literal_eval(
                                '["' + x["income_increases_for_every_year"] + '"]'
                            )
                else:
                    if d.get(ik):
                        d[ik].append(iv)
                    else:
                        d[ik] = ast.literal_eval('["' + iv + '"]')

        d["additional_income_nums"] = ast.literal_eval(
            '["' + d["additional_income_nums"] + '"]'
        )

    elif k == "expenses_details":
        for ik, iv in v.items():
            if ik == "taxes":
                d["expense_taxes"] = ast.literal_eval('["' + iv["expense_taxes"] + '"]')
                d["taxes_ye_mo"] = ast.literal_eval('["' + iv["taxes_ye_mo"] + '"]')
                d["taxes_frequency"] = ast.literal_eval(
                    '["' + iv["taxes_frequency"] + '"]'
                )
                d["taxes_increase_value"] = iv["taxes_increase_value"]
                d["taxes_increases_type"] = iv["taxes_increases_type"]
                d["taxes_increases_for_every_year"] = iv[
                    "taxes_increases_for_every_year"
                ]

            elif ik == "insurance":
                d["insurance_expense"] = ast.literal_eval(
                    '["' + iv["insurance_expense"] + '"]'
                )
                d["insu_ye_mo"] = ast.literal_eval('["' + iv["insu_ye_mo"] + '"]')
                d["insu_frequency"] = ast.literal_eval(
                    '["' + iv["insu_frequency"] + '"]'
                )
                d["insu_increase_value"] = iv["insu_increase_value"]
                d["insu_increases_type"] = iv["insu_increases_type"]
                d["insu_increases_for_every_year"] = iv["insu_increases_for_every_year"]
            elif ik == "hoa":
                d["expense_hoa"] = ast.literal_eval('["' + iv["expense_hoa"] + '"]')
                d["hoa_ye_mo"] = ast.literal_eval('["' + iv["hoa_ye_mo"] + '"]')
                d["hoa_frequency"] = ast.literal_eval('["' + iv["hoa_frequency"] + '"]')
                d["hoa_increase_value"] = iv["hoa_increase_value"]
                d["hoa_increases_type"] = iv["hoa_increases_type"]
                d["hoa_increases_for_every_year"] = iv["hoa_increases_for_every_year"]

    elif k == "other_expenses":
        for ik, iv in v.items():
            d[ik] = ast.literal_eval('["' + iv + '"]')

    elif k == "additional_expenses":
        d["additional_expenses_nums"] = ""
        for index, x in enumerate(v):
            if index != len(v) - 1:
                d["additional_expenses_nums"] = (
                    d["additional_expenses_nums"] + str(index) + ","
                )
            else:
                d["additional_expenses_nums"] = d["additional_expenses_nums"] + str(
                    index
                )
            for ik, iv in x.items():
                if ik == "frequency_data":
                    for x in iv:
                        if d.get("expense_increase_value" + "[" + str(index) + "]"):
                            d["expense_increase_value" + "[" + str(index) + "]"].append(
                                x["expense_increase_value"]
                            )
                            d["expense_increases_type" + "[" + str(index) + "]"].append(
                                x["expense_increases_type"]
                            )
                            d[
                                "expense_increases_for_every_year"
                                + "["
                                + str(index)
                                + "]"
                            ].append(x["expense_increases_for_every_year"])
                        else:
                            d[
                                "expense_increase_value" + "[" + str(index) + "]"
                            ] = ast.literal_eval(
                                '["' + x["expense_increase_value"] + '"]'
                            )
                            d[
                                "expense_increases_type" + "[" + str(index) + "]"
                            ] = ast.literal_eval(
                                '["' + x["expense_increases_type"] + '"]'
                            )
                            d[
                                "expense_increases_for_every_year"
                                + "["
                                + str(index)
                                + "]"
                            ] = ast.literal_eval(
                                '["' + x["expense_increases_for_every_year"] + '"]'
                            )
                else:
                    if d.get(ik):
                        d[ik].append(iv)
                    else:
                        d[ik] = ast.literal_eval('["' + iv + '"]')
        d["additional_expenses_nums"] = ast.literal_eval(
            '["' + d["additional_expenses_nums"] + '"]'
        )

print(d)


# post_dict = {}

# tenant_name = post_dict.get("tenant_name")[0]
# property_mgmt_type = int(post_dict.get("property_mgmt_type")[0])
# expense_vacancy_type = int(post_dict.get("expense_vacancy_type")[0])
# expense_maintenance_type = int(post_dict.get("expense_maintenance_type")[0])
# balance = 0
# if post_dict.get("original_purchase_price")[0]:
#     balance = float(post_dict.get("original_purchase_price")[0])
# closing_concession = post_dict.get("closing_consessions_view")[0]
# if not closing_concession.strip():
#     closing_concession = 0
# closing_expenses = post_dict.get("closing_expenses_view")[0]
# if not closing_expenses.strip():
#     closing_expenses = 0

# sft_leased = post_dict.get("sft_leased")[0]

# if not sft_leased:
#     sft_leased = 0
# else:
#     sft_leased = int(sft_leased)

# lease_rate = post_dict.get("lease_rate")[0]

# if not lease_rate:
#     lease_rate = 0
# else:
#     lease_rate = int(lease_rate)

# gross_income = post_dict.get("gross_income")[0]
# rent_increases = post_dict.get("rent_increases")[0]
# rent_increase_value = post_dict.get("rent_increase_value")[0]
# rent_increases_for_every_year = post_dict.get("rent_increases_for_every_year")[0]
# amount_down_payment_type = int(post_dict.get("amount_down_payment_type")[0])
# if post_dict.get("amount_down_payment_value")[0]:
#     amount_down_payment_value = float(post_dict.get("amount_down_payment_value")[0])
# else:
#     amount_down_payment_value = 0
# if not amount_down_payment_value:
#     amount_down_payment_value = 0

# asset_appraisal_type = int(post_dict.get("asset_appraisal_type")[0])
# if post_dict.get("asset_appraisal_value")[0]:
#     asset_appraisal_value = float(post_dict.get("asset_appraisal_value")[0])
# else:
#     asset_appraisal_value = 0
# sales_expense_type = int(post_dict.get("sales_expense_type")[0])
# if post_dict.get("sales_expense_value")[0]:
#     sales_expense_value = float(post_dict.get("sales_expense_value")[0])
# else:
#     sales_expense_value = 0

# lease_rate_type = post_dict.get("lease_rate_type")[0]

# if post_dict.get("expense_maintenance")[0]:
#     expense_maintenance = float(post_dict.get("expense_maintenance")[0])
# else:
#     expense_maintenance = 0
# if post_dict.get("expense_vacancy")[0]:
#     expense_vacancy = float(post_dict.get("expense_vacancy")[0])
# else:
#     expense_vacancy = 0
# if post_dict.get("property_mgmt")[0]:
#     property_mgmt = float(post_dict.get("property_mgmt")[0])
# else:
#     property_mgmt = 0
# if post_dict.get("expense_taxes")[0]:
#     expense_taxes = int(post_dict.get("expense_taxes")[0])
# else:
#     expense_taxes = 0
# taxes_ye_mo = int(post_dict.get("taxes_ye_mo")[0])
# taxes_frequency = int(post_dict.get("taxes_frequency")[0])
# taxes_increases_type = int(post_dict.get("taxes_increases_type")[0])
# if post_dict.get("taxes_increase_value")[0]:
#     taxes_increase_value = int(post_dict.get("taxes_increase_value")[0])
# else:
#     taxes_increase_value = 0
# if post_dict.get("taxes_increases_for_every_year")[0]:
#     taxes_increases_for_every_year = int(
#         post_dict.get("taxes_increases_for_every_year")[0]
#     )
# else:
#     taxes_increases_for_every_year = 0

# if post_dict.get("expense_hoa")[0]:
#     expense_hoa = float(post_dict.get("expense_hoa")[0])
# else:
#     expense_hoa = 0
# hoa_ye_mo = int(post_dict.get("hoa_ye_mo")[0])
# hoa_frequency = int(post_dict.get("hoa_frequency")[0])
# hoa_increases_type = int(post_dict.get("hoa_increases_type")[0])
# if post_dict.get("hoa_increase_value")[0]:
#     hoa_increase_value = float(post_dict.get("hoa_increase_value")[0])
# else:
#     hoa_increase_value = 0
# hoa_increases_for_every_year = int(post_dict.get("hoa_increases_for_every_year")[0])
# if post_dict.get("insurance_expense")[0]:
#     insurance_expense = float(post_dict.get("insurance_expense")[0])
# else:
#     insurance_expense = 0
# insu_ye_mo = int(post_dict.get("insu_ye_mo")[0])
# insu_frequency = int(post_dict.get("insu_frequency")[0])
# insu_increases_type = int(post_dict.get("insu_increases_type")[0])
# if post_dict.get("insu_increase_value")[0]:
#     insu_increase_value = float(post_dict.get("insu_increase_value")[0])
# else:
#     insu_increase_value = 0
# insu_increases_for_every_year = int(post_dict.get("insu_increases_for_every_year")[0])
# if post_dict.get("ammortization_years")[0]:
#     ammortization_years = int(post_dict.get("ammortization_years")[0])
# else:
#     ammortization_years = 0
# ammortization_years = ammortization_years * 12
# if post_dict.get("annual_rate_interests")[0]:
#     annual_rate_interests = float(post_dict.get("annual_rate_interests")[0])
# else:
#     annual_rate_interests = 0
# if amount_down_payment_type == 0:
#     amount_down_payment = balance * 0.01 * amount_down_payment_value
# else:
#     amount_down_payment = int(amount_down_payment_value)
# if lease_rate_type == 0:
#     gross_income = sft_leased * lease_rate
# else:
#     gross_income = lease_rate * 12
# if gross_income:
#     residential_data["dynamic_input_update"]["gross_income"] = gross_income

# noi = int(gross_income) - int(gross_income) * 0.01
# if noi:
#     residential_data["dynamic_input_update"]["noi"] = noi
# if balance:
#     cap_rate = noi / balance * 100
# else:
#     cap_rate = 0
# if cap_rate:
#     residential_data["dynamic_input_update"]["cap_rate"] = round(cap_rate, 2)

# if amount_down_payment != None:
#     residential_data["dynamic_input_update"][
#         "amount_down_payment"
#     ] = amount_down_payment
#     residential_data["dynamic_input_update"]["mortgage_loan"] = (
#         balance - amount_down_payment
#     )
#     mortgage_loan = balance - amount_down_payment
# interestRate = 0.036
# if post_dict.get("no_years")[0]:
#     terms = int(post_dict.get("no_years")[0])
# else:
#     terms = 0


a = {
    "property_details": {
        "borrower_name": "",
        "property_type": "Multi-Family",
        "no_units": "",
        "approximate_sq_footage": "",
    },
    "loan_terms": {
        "property_value": "",
        "loan_amount": "",
        "ltv": "",
        "amortization_years": "25",
        "interest_rate": "4",
        "down_payment": "",
        "dscr_ratio": "",
    },
    "income": {"gross_annual_rental": "", "other_income": "0"},
    "annual_operating_expenses": {
        "utilities_telephone": "0",
        "repairs_maintenance": "0",
        "salaries_legal": "0",
        "snow_trash": "0",
        "re_taxes": "0",
        "insurance": "0",
        "other_operating_exp": "0",
        "annual_operating_exp": "0",
        "mgmt_fees": "0",
    },
}


d = {}
print(a)
for k, v in a.items():
    for ik, iv in v.items():
        d[ik] = iv
print(d)


a = {
    "analysis_type": "1",
    "property_details": {
        "asset_name": "",
        "original_purchase_price": "",
        "acquired_on": "2021",
        "no_years": "10",
        "total_sft": "",
        "no_units": "1",
        "asset_appraisal_value": "5",
        "asset_appraisal_type": "0",
        "sales_expense_value": "5",
        "sales_expense_type": "0",
        "ammortization_years": "25",
        "annual_rate_interests": "",
        "debt_service_ratio": "0",
        "avg_exp": "4",
        "expense_vacancy": "4",
        "expense_vacancy_type": "0",
    },
    "loan_details": {
        "amount_down_payment_value": "25",
        "amount_down_payment_type": "0",
        "amount_down_payment": "0",
        "mortgage_loan": "0",
        "gross_income": "",
        "noi": "",
        "cap_rate": "",
        "year1_roi": "",
        "total_roi_percentage": "",
        "total_roi": "",
    },
    "closing_detials": {
        "closing_consession": [
            {
                "closing_consessions_view": "0",
                "closing_consession_name": "Closing Concession",
                "closing_consessionamount": "0",
            }
        ],
        "closing_expense": [
            {
                "closing_expenses_view": "0",
                "closing_expensename": "Closing Expenses",
                "closing_expenseamount": "0",
            }
        ],
    },
    "tenant_details": [
        {
            "tenant_name": "Tenant1",
            "sft_leased": "8",
            "lease_rate": "",
            "lease_rate_type": "0",
            "rent_frequency": "0",
            "frequency_data": [
                {
                    "rent_increase_value": "0",
                    "rent_increases": "0",
                    "rent_increases_for_every_year": "1",
                }
            ],
        },
        {
            "tenant_name": "",
            "sft_leased": "",
            "lease_rate": "",
            "lease_rate_type": "0",
            "rent_frequency": "0",
            "frequency_data": [
                {
                    "" "rent_increase_value": "0",
                    "rent_increases": "0",
                    "rent_increases_for_every_year": "1",
                }
            ],
        },
        {
            "tenant_name": "",
            "sft_leased": "",
            "lease_rate": "",
            "lease_rate_type": "0",
            "rent_frequency": "0",
            "frequency_data": [
                {
                    "rent_increase_value": "0",
                    "rent_increases": "0",
                    "rent_increases_for_every_year": "1",
                }
            ],
        },
    ],
    "reimbursement_details": {
        "reimbursement_income": "0",
        "reim_ye_mo": "0",
        "reim_frequency": "0",
        "reim_increase_value": ["0"],
        "reim_increases_type": ["0"],
        "reim_increases_for_every_year": ["1"],
    },
    "additional_income_details": [
        {
            "income_name": "",
            "income_amount": "",
            "income_frequency": "0",
            "frequency_data": [
                {
                    "income_increase_value": "0",
                    "income_increases_type": "0",
                    "income_increases_for_every_year": "1",
                },
                {
                    "income_increase_value": "0",
                    "income_increases_type": "0",
                    "income_increases_for_every_year": "1",
                },
            ],
        }
    ],
    "expenses_details": {
        "taxes": {
            "expense_taxes": "0",
            "taxes_ye_mo": "0",
            "taxes_frequency": "0",
            "taxes_increase_value": ["0"],
            "taxes_increases_type": ["0"],
            "taxes_increases_for_every_year": ["1"],
        },
        "insurance": {
            "insurance_expense": "0",
            "insu_ye_mo": "0",
            "insu_frequency": "0",
            "insu_increase_value": ["0"],
            "insu_increases_type": ["0"],
            "insu_increases_for_every_year": ["1"],
        },
        "common_area_maintenance": {
            "expense_cam": "0",
            "cam_ye_mo": "0",
            "cam_frequency": "0",
            "cam_increase_value": ["0"],
            "cam_increases_type": ["0"],
            "cam_increases_for_every_year": ["1"],
        },
        "utilities": {
            "expense_utilities": "0",
            "utilities_ye_mo": "0",
            "utilities_frequency": "0",
            "utilities_increase_value": ["0"],
            "utilities_increases_type": ["0"],
            "utilities_increases_for_every_year": ["1"],
        },
        "hoa": {
            "expense_hoa": "0",
            "hoa_ye_mo": "0",
            "hoa_frequency": "0",
            "hoa_increase_value": ["0"],
            "hoa_increases_type": ["0"],
            "hoa_increases_for_every_year": ["1"],
        },
        "management_fee": {
            "expense_management": "0",
            "management_ye_mo": "0",
            "management_frequency": "0",
            "management_increase_value": ["0"],
            "management_increases_type": ["0"],
            "management_increases_for_every_year": ["1"],
        },
        "administrative_fee": {
            "expense_administrative": "0",
            "administrative_ye_mo": "0",
            "administrative_frequency": "0",
            "administrative_increase_value": ["0"],
            "administrative_increases_type": ["0"],
            "administrative_increases_for_every_year": ["1"],
        },
    },
    "additional_expenses": [
        {
            "expense_head_name": "",
            "expense_amount": "",
            "expense_frequency": "0",
            "frequency_data": [
                {
                    "expense_increase_value": "0",
                    "expense_increases_type": "0",
                    "expense_increases_for_every_year": "1",
                }
            ],
        },
    ],
}


print(a)


def convert_roi_api_data(req_data):
    d = {}
    a = req_data
    for k, v in a.items():
        if k == "analysis_type":
            d["analysis_type"] = ast.literal_eval('["' + a[k] + '"]')
        elif k == "property_details":
            for ik, iv in v.items():
                d[ik] = ast.literal_eval('["' + iv + '"]')

        elif k == "loan_details":
            for ik, iv in v.items():
                d[ik] = ast.literal_eval('["' + iv + '"]')

        elif k == "closing_detials":
            for ik, iv in v.items():
                if ik == "closing_consession":
                    for x in iv:
                        d["closing_consessions_view"] = ast.literal_eval(
                            '["' + x["closing_consessions_view"] + '"]'
                        )
                        d["closing_consession_name"] = ast.literal_eval(
                            '["' + x["closing_consession_name"] + '"]'
                        )
                        d["closing_consessionamount"] = ast.literal_eval(
                            '["' + x["closing_consessionamount"] + '"]'
                        )
                if ik == "closing_expense":
                    for x in iv:
                        d["closing_expenses_view"] = ast.literal_eval(
                            '["' + x["closing_expenses_view"] + '"]'
                        )
                        d["closing_expensename"] = ast.literal_eval(
                            '["' + x["closing_expensename"] + '"]'
                        )
                        d["closing_expenseamount"] = ast.literal_eval(
                            '["' + x["closing_expenseamount"] + '"]'
                        )

        elif k == "tenant_details":
            d["tenant_nums"] = ""
            for index, x in enumerate(v):
                if index != len(v) - 1:
                    d["tenant_nums"] = d["tenant_nums"] + str(index) + ","
                else:
                    d["tenant_nums"] = d["tenant_nums"] + str(index)
                for ik, iv in x.items():
                    if ik == "frequency_data":
                        for x in iv:
                            if d.get("rent_increase_value" + "[" + str(index) + "]"):
                                d[
                                    "rent_increase_value" + "[" + str(index) + "]"
                                ].append(x["rent_increase_value"])
                                d["rent_increases" + "[" + str(index) + "]"].append(
                                    x["rent_increases"]
                                )
                                d[
                                    "rent_increases_for_every_year"
                                    + "["
                                    + str(index)
                                    + "]"
                                ].append(x["rent_increases_for_every_year"])
                            else:
                                d[
                                    "rent_increase_value" + "[" + str(index) + "]"
                                ] = ast.literal_eval(
                                    '["' + x["rent_increase_value"] + '"]'
                                )
                                d[
                                    "rent_increases" + "[" + str(index) + "]"
                                ] = ast.literal_eval('["' + x["rent_increases"] + '"]')
                                d[
                                    "rent_increases_for_every_year"
                                    + "["
                                    + str(index)
                                    + "]"
                                ] = ast.literal_eval(
                                    '["' + x["rent_increases_for_every_year"] + '"]'
                                )
                    else:
                        if d.get(ik):
                            d[ik].append(iv)
                        else:
                            d[ik] = ast.literal_eval('["' + iv + '"]')

            d["tenant_nums"] = ast.literal_eval('["' + d["tenant_nums"] + '"]')

        elif k == "additional_income_details":
            d["additional_income_nums"] = ""
            for index, x in enumerate(v):
                if index != len(v) - 1:
                    d["additional_income_nums"] = (
                        d["additional_income_nums"] + str(index) + ","
                    )
                else:
                    d["additional_income_nums"] = d["additional_income_nums"] + str(
                        index
                    )
                for ik, iv in x.items():
                    if ik == "frequency_data":
                        for x in iv:
                            if d.get("income_increase_value" + "[" + str(index) + "]"):
                                d[
                                    "income_increase_value" + "[" + str(index) + "]"
                                ].append(x["income_increase_value"])
                                d[
                                    "income_increases_type" + "[" + str(index) + "]"
                                ].append(x["income_increases_type"])
                                d[
                                    "income_increases_for_every_year"
                                    + "["
                                    + str(index)
                                    + "]"
                                ].append(x["income_increases_for_every_year"])
                            else:
                                d[
                                    "income_increase_value" + "[" + str(index) + "]"
                                ] = ast.literal_eval(
                                    '["' + x["income_increase_value"] + '"]'
                                )
                                d[
                                    "income_increases_type" + "[" + str(index) + "]"
                                ] = ast.literal_eval(
                                    '["' + x["income_increases_type"] + '"]'
                                )
                                d[
                                    "income_increases_for_every_year"
                                    + "["
                                    + str(index)
                                    + "]"
                                ] = ast.literal_eval(
                                    '["' + x["income_increases_for_every_year"] + '"]'
                                )
                    else:
                        if d.get(ik):
                            d[ik].append(iv)
                        else:
                            d[ik] = ast.literal_eval('["' + iv + '"]')

            d["additional_income_nums"] = ast.literal_eval(
                '["' + d["additional_income_nums"] + '"]'
            )
        elif k == "reimbursement_details":
            d["reimbursement_income"] = ast.literal_eval(
                '["' + v["reimbursement_income"] + '"]'
            )
            d["reim_ye_mo"] = ast.literal_eval('["' + v["reim_ye_mo"] + '"]')
            d["reim_frequency"] = ast.literal_eval('["' + v["reim_frequency"] + '"]')
            d["reim_increase_value"] = v["reim_increase_value"]
            d["reim_increases_type"] = v["reim_increases_type"]
            d["reim_increases_for_every_year"] = v["reim_increases_for_every_year"]

        elif k == "expenses_details":
            for ik, iv in v.items():
                if ik == "taxes":
                    d["expense_taxes"] = ast.literal_eval(
                        '["' + iv["expense_taxes"] + '"]'
                    )
                    d["taxes_ye_mo"] = ast.literal_eval('["' + iv["taxes_ye_mo"] + '"]')
                    d["taxes_frequency"] = ast.literal_eval(
                        '["' + iv["taxes_frequency"] + '"]'
                    )
                    d["taxes_increase_value"] = iv["taxes_increase_value"]
                    d["taxes_increases_type"] = iv["taxes_increases_type"]
                    d["taxes_increases_for_every_year"] = iv[
                        "taxes_increases_for_every_year"
                    ]

                elif ik == "insurance":
                    d["insurance_expense"] = ast.literal_eval(
                        '["' + iv["insurance_expense"] + '"]'
                    )
                    d["insu_ye_mo"] = ast.literal_eval('["' + iv["insu_ye_mo"] + '"]')
                    d["insu_frequency"] = ast.literal_eval(
                        '["' + iv["insu_frequency"] + '"]'
                    )
                    d["insu_increase_value"] = iv["insu_increase_value"]
                    d["insu_increases_type"] = iv["insu_increases_type"]
                    d["insu_increases_for_every_year"] = iv[
                        "insu_increases_for_every_year"
                    ]
                elif ik == "hoa":
                    d["expense_hoa"] = ast.literal_eval('["' + iv["expense_hoa"] + '"]')
                    d["hoa_ye_mo"] = ast.literal_eval('["' + iv["hoa_ye_mo"] + '"]')
                    d["hoa_frequency"] = ast.literal_eval(
                        '["' + iv["hoa_frequency"] + '"]'
                    )
                    d["hoa_increase_value"] = iv["hoa_increase_value"]
                    d["hoa_increases_type"] = iv["hoa_increases_type"]
                    d["hoa_increases_for_every_year"] = iv[
                        "hoa_increases_for_every_year"
                    ]
                elif ik == "common_area_maintenance":
                    d["expense_cam"] = ast.literal_eval('["' + iv["expense_cam"] + '"]')
                    d["cam_ye_mo"] = ast.literal_eval('["' + iv["cam_ye_mo"] + '"]')
                    d["cam_frequency"] = ast.literal_eval(
                        '["' + iv["cam_frequency"] + '"]'
                    )
                    d["cam_increase_value"] = iv["cam_increase_value"]
                    d["cam_increases_type"] = iv["cam_increases_type"]
                    d["cam_increases_for_every_year"] = iv[
                        "cam_increases_for_every_year"
                    ]
                elif ik == "utilities":
                    d["expense_utilities"] = ast.literal_eval(
                        '["' + iv["expense_utilities"] + '"]'
                    )
                    d["utilities_ye_mo"] = ast.literal_eval(
                        '["' + iv["utilities_ye_mo"] + '"]'
                    )
                    d["utilities_frequency"] = ast.literal_eval(
                        '["' + iv["utilities_frequency"] + '"]'
                    )
                    d["utilities_increase_value"] = iv["utilities_increase_value"]
                    d["utilities_increases_type"] = iv["utilities_increases_type"]
                    d["utilities_increases_for_every_year"] = iv[
                        "utilities_increases_for_every_year"
                    ]
                elif ik == "management_fee":
                    d["expense_management"] = ast.literal_eval(
                        '["' + iv["expense_management"] + '"]'
                    )
                    d["management_ye_mo"] = ast.literal_eval(
                        '["' + iv["management_ye_mo"] + '"]'
                    )
                    d["management_frequency"] = ast.literal_eval(
                        '["' + iv["management_frequency"] + '"]'
                    )
                    d["management_increase_value"] = iv["management_increase_value"]
                    d["management_increases_type"] = iv["management_increases_type"]
                    d["management_increases_for_every_year"] = iv[
                        "management_increases_for_every_year"
                    ]
                elif ik == "administrative_fee":
                    d["expense_administrative"] = ast.literal_eval(
                        '["' + iv["expense_administrative"] + '"]'
                    )
                    d["administrative_ye_mo"] = ast.literal_eval(
                        '["' + iv["administrative_ye_mo"] + '"]'
                    )
                    d["administrative_frequency"] = ast.literal_eval(
                        '["' + iv["administrative_frequency"] + '"]'
                    )
                    d["administrative_increase_value"] = iv[
                        "administrative_increase_value"
                    ]
                    d["administrative_increases_type"] = iv[
                        "administrative_increases_type"
                    ]
                    d["administrative_increases_for_every_year"] = iv[
                        "administrative_increases_for_every_year"
                    ]

        elif k == "additional_expenses":
            d["additional_expenses_nums"] = ""
            for index, x in enumerate(v):
                if index != len(v) - 1:
                    d["additional_expenses_nums"] = (
                        d["additional_expenses_nums"] + str(index) + ","
                    )
                else:
                    d["additional_expenses_nums"] = d["additional_expenses_nums"] + str(
                        index
                    )
                for ik, iv in x.items():
                    if ik == "frequency_data":
                        for x in iv:
                            if d.get("expense_increase_value" + "[" + str(index) + "]"):
                                d[
                                    "expense_increase_value" + "[" + str(index) + "]"
                                ].append(x["expense_increase_value"])
                                d[
                                    "expense_increases_type" + "[" + str(index) + "]"
                                ].append(x["expense_increases_type"])
                                d[
                                    "expense_increases_for_every_year"
                                    + "["
                                    + str(index)
                                    + "]"
                                ].append(x["expense_increases_for_every_year"])
                            else:
                                d[
                                    "expense_increase_value" + "[" + str(index) + "]"
                                ] = ast.literal_eval(
                                    '["' + x["expense_increase_value"] + '"]'
                                )
                                d[
                                    "expense_increases_type" + "[" + str(index) + "]"
                                ] = ast.literal_eval(
                                    '["' + x["expense_increases_type"] + '"]'
                                )
                                d[
                                    "expense_increases_for_every_year"
                                    + "["
                                    + str(index)
                                    + "]"
                                ] = ast.literal_eval(
                                    '["' + x["expense_increases_for_every_year"] + '"]'
                                )
                    else:
                        if d.get(ik):
                            d[ik].append(iv)
                        else:
                            d[ik] = ast.literal_eval('["' + iv + '"]')
            d["additional_expenses_nums"] = ast.literal_eval(
                '["' + d["additional_expenses_nums"] + '"]'
            )

    print(d)
    return d


convert_roi_api_data(a)
