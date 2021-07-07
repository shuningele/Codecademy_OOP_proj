class Applicant:

  def __init__(self, name, currency="GBP", public_sponsorship = 0):
    currency_exchange_rates = {"CNY":8.9427,"USD":1.3812,"CAD":1.7176,"EUR":1.1674, "GBP":1}
    london_living_cost_per_month_GBP = 1334
    outside_of_london_living_cost_GBP = 1023
    count = 1
    
    self.id = count
    Applicant.count += 1
    print(f"Creating applicant info: {name}, applicant ID {self.id}, all fees entered should be in {currency}.")
    self.name = name
    self.currency = currency
    self.unis = {}
    self.total_cost = 0
    self.public_sponsorship = public_sponsorship


  def __repr__(self):
    unis = ""
    for uni in unis.keys():
      unis += uni+"\n"
    return "Applicant name: {0}\nUniversities: \n{1}Record Currency: {2}".format(self.name, unis, self.currency)


  def add_uni_info(self, uni_name, years_left_in_degree, degree_title, tuition_fee_by_year, city, residential_months_per_year, custom = None):
    self.unis[uni_name]={"total tuition fee":years_left_in_degree*tuition_fee_by_year, "living cost per year (est.)":0, "city":city, "residential months per year":residential_months_per_year, "custom living cost per year":custom, "years left in degree":years_left_in_degree}
    self.program_title = degree_title
    
    if city.lower()=="london" and custom is None:
      self.unis[uni_name]["living cost per year (est.)"] = self.currency_exchange_rates[self.currency]*self.london_living_cost_per_month_GBP*residential_months_per_year
      self.unis[uni_name]["total cost"] = self.unis[uni_name]["living cost per year (est.)"]*years_left_in_degree + self.unis[uni_name]["total tuition fee"] - self.public_sponsorship

    elif city.lower()!= "london" and custom is None:
      self.unis[uni_name]["living_cost_per_year (est.)"] = self.currency_exchange_rates[self.currency]*self.outside_of_london_living_cost_GBP*residential_months_per_year
      self.unis[uni_name]["total_cost"] = self.unis[uni_name]["living_cost_per_year (est.)"]*years_left_in_degree + self.unis[uni_name]["total tuition fee"] - self.public_sponsorship

    else:
      self.customise_living_cost(uni_name, custom)

    print(f"Entry added for {uni_name}:\n{self.unis[uni_name]}")


  def customise_living_cost(self, uni_name, living_cost_per_month):
    self.unis[uni_name]["living cost per year (est.)"] = living_cost_per_month*self.unis[uni_name]["residential_months_per_year"] 
    self.unis[uni_name]["total cost"] = self.unis[uni_name]["living cost per year (est.)"]*self.unis[uni_name]["years left in degree"] + self.unis[uni_name]["total_tuition_fee"] - self.public_sponsorship
    print("Living cost customised. ")


  def add_uni_specific_scholorship_or_award(self, uni_name, fund_name, amount):
    self.unis[uni_name]["total cost"] -= amount
    if "bursaries" in self.unis[uni_name]:
      self.unis[uni_name]["bursaries"] += fund_name
    else:
      self.unis[uni_name]["bursaries"] = fund_name