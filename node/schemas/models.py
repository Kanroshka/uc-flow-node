from typing import Literal, List, Union
from datetime import date

from pydantic import BaseModel, constr


# Поля customer

class CustomerId(BaseModel):
    customer_id: int

class CustomerName(BaseModel):
    customer_name: constr(max_length=50)

class CustomerBranchIds(BaseModel):
    customer_branch_ids: int

class CustomerTeacherIds(BaseModel):
    customer_teacher_ids: List[int]

class CustomerIsStudy(BaseModel):
    customer_is_study: int

class CustomerStudyStatusId(BaseModel):
    customer_study_status_id: str

class CustomerLeadStatusId(BaseModel):
    customer_lead_status_id: int

class CustomerLeadSourceId(BaseModel):
    customer_lead_source_id: int

class CustomerAssignedId(BaseModel):
    customer_assigned_id: int

class CustomerLegalType(BaseModel):
    customer_legal_type: int

class CustomerLegalName(BaseModel):
    customer_legal_name: constr(max_length=50)

class CustomerCompanyId(BaseModel):
    customer_company_id: int

class CustomerDob(BaseModel): 
    customer_dob: date

class CustomerBalance(BaseModel): 
    customer_balance: float

class CustomerPaidLessonCount(BaseModel):
    customer_paid_lesson_count: int

class CustomerPhone(BaseModel):
    customer_phone: str

class CustomerEmail(BaseModel):
    customer_email: str

class CustomerWeb(BaseModel):
    customer_web: str

class CustomerAddr(BaseModel):
    customer_addr: str

class CustomerNote(BaseModel):
    customer_note: str


# поля для фильрации
class CustomerGender(BaseModel):
    customer_gender: str

class CustomerAgeFrom(BaseModel):
    customer_age_from: int

class CustomerAgeTo(BaseModel):
    customer_age_to: int

class CustomerLessonCountFrom(BaseModel):
    customer_lesson_count_from: int

class CustomerLessonCountTo(BaseModel):
    customer_lesson_count_to: int

class CustomerBalanceContractFrom(BaseModel):
    customer_balance_contract_from: int

class CustomerBalanceContractTo(BaseModel):
    customer_balance_contract_to: int

class CustomerBalanceBonusFrom(BaseModel):
    customer_balance_bonus_from: int

class CustomerBalanceBonusTo(BaseModel):
    customer_balance_bonus_to: int

class CustomerRemoved(BaseModel):
    customer_removed: int

class CustomerRemovedFrom(BaseModel):
    customer_removed_from: date

class CustomerRemovedTo(BaseModel):
    customer_removed_to: date

class CustomerLevelId(BaseModel):
    customer_level_id: int

class CustomerEmployeeId(BaseModel):
    customer_employee_id: int

class CustomerColor(BaseModel):
    customer_color: int

class CustomerDateFrom(BaseModel):
    customer_date_from: date 

class CustomerDateTo(BaseModel):
    customer_date_to: date

class CustomerNextLessonDateFrom(BaseModel):
    customer_next_lesson_date_from: date

class CustomerNextLessonDateTo(BaseModel):
    customer_next_lesson_date_to: date

class CustomerTariffTillFrom(BaseModel):
    customer_tariff_till_from: date

class CustomerTariffTillTo(BaseModel):
    customer_tariff_till_to: date

class CustomerRejectId(BaseModel):
    customer_reject_id: int

class CustomerComment(BaseModel):
    customer_comment: str

class CustomerDobFrom(BaseModel):
    customer_dob_from: date

class CustomerDobTo(BaseModel):
    customer_dob_to: date

class CustomerWithGroupsTrue(BaseModel):
    customer_with_groups_true: str
