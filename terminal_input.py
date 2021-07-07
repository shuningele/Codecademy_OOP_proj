from uni_fees import Applicant

applicants_info = {}
def add_applicant(id, applicant):
  applicants_info[id] = applicant


def initialise_or_retreive_applicant(): 
  initialise = input("Enter 1 for initialising an applicant, 2 for editing existing applicant information.").strip()
  if initialise == "1":
    applicant_name = input("Enter applicant's name")
    general_bursary = int(input("Enter the amount of a general bursary if one is available, which funds you on your application to any university: (Enter 0 if none is available) "))
    x = input(f"Enter the appropriate abbreviation for the currency you wish to use for {applicant_name}'s records: (eg. CNY, GBP) ").strip()
    new_applicant = Applicant(applicant_name, x, general_bursary) 
    add_applicant[new_applicant.id] = new_applicant
  elif initialise == "2":
    app_id = int(input("Enter applicant ID: ").strip())
    try:
      current_applicant = applicants_info[app_id]
    except:
      print("Invalid applicant ID, start over with another ID")
  else:
    print("Invalid input, start again. ")


