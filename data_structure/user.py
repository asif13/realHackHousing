


class user_profile:
    def __init__(self, status, sport, office, school,
                  food, region, budget_min,budget_max, gender):
        self.status = status
        self.sport = sport # list of sports
        self.office = office  # office location as land profiles
        self.school = school  #of type location
        self.food = food
        self.religion = region # class region
        self.budget_min = budget_min 
        self.budget_max = budget_max
        self.gender = gender
        