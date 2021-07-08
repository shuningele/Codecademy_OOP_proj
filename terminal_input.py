from applicant import Applicant


def initialise_or_retrieve_applicant(): 
  initialise = input("Enter 1 for initialising an applicant, 2 for editing existing applicant information.").strip()
  if initialise == "1":
    applicant_name = input("Enter applicant's name")
    general_bursary = int(input("Enter the amount of a general bursary if one is available, which funds you on your application to any university: (Enter 0 if none is available) "))
    x = input(f"Enter the appropriate abbreviation for the currency you wish to use for {applicant_name}'s records: (eg. CNY, GBP) ").strip()
    new_applicant = Applicant(applicant_name, x, general_bursary) 
    
  elif initialise == "2":
    app_id = int(input("Enter applicant ID: ").strip())
    try:
      current_applicant = Applicant.applicants_info[app_id]
    except:
      again = input("Invalid applicant ID, enter 1 to initialise a new applicant or retrieve applicant info with another ID")
      if again =="1":
        initialise_or_retrieve_applicant()

  else:
    again = input("Invalid input, enter y to start again")
    if again == "y":
      initialise_or_retrieve_applicant()


def add_uni_info_with_usr_input():
  id = input("Enter applicant ID:")
  try:
    applicant = Applicant.retrieve_applicant(id)
    un = input("Enter the name of the university for which you'd like to create a total cost entry:")
    yfid = input("Enter years left for which tuition fee and living cost should be calculated")
    dt = input(" Enter the title of the program, eg. Physics Bsc: " )
    tfby = float(input("Enter the annual tuition fee of this program at this uni: "))
    ct = input("Enter the UK city you'll be residing in while completing the program, eg. London:")
    rmpy = int(input("Enter how many months each year is expected to progress through the program and for which tenancy contract can be signed if applicable:"))
    cus = input("According to the UK government's financial proof requirement, monthly living cost in London has been default to 1334 GBP, that of outside London has been default to 1023 GBP per year. Would you like to customise estimated monthly living cost? Enter yes or no")
    if cus.lower() == "yes":
      cus = int(input("Enter a monthly living cost:"))
    else:
      cus = None

    # uni_name, years_left_in_degree, degree_title, tuition_fee_by_year, city, residential_months_per_year, custom = None
    applicant.add_uni_info(un, yfid, dt, tfby, ct, rmpy, cus)

  except:
    again = input("invalid ID, try again with a new ID by entering y. ")
    if again =="y":
      add_uni_info_with_usr_input()
  


