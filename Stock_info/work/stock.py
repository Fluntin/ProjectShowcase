class Stock:
    def __init__(self, company_name, debt_to_equity, pe, ps, history, omx):
        # An object of type Stock contains all the info that describes a company, both technical and fundamental.
        # Note: history -> {date: price}
        # Note: omx -> {date: price}

        self.company_name = company_name
        self.debt_to_equity = debt_to_equity
        self.pe = pe
        self.ps = ps
        self.history = history
        self.omx = omx
        self.course_development = self.calculate_course_development()
        self.course_highest = self.calculate_course_highest()
        self.course_lowest = self.calculate_course_lowest()
        self.betha = self.calculate_betha()

    def calculate_course_development(self):
        # Calculate course development for the last 30 days.
        # Input: self
        # Output: course development for the last 30 days -> float

        values = [float(self.history[key]) for key in self.history]
        course_development = ((values[-1] - values[0]) / values[0]) * 100

        return round(course_development, 2)

    def calculate_course_lowest(self):
        # Calculate the lowest value for the last 30 days.
        # Input: self
        # Output: lowest value for the last 30 days -> float
        values = [float(self.history[key]) for key in self.history]
        return min(values)

    def calculate_course_highest(self):
        # Calculate the highest value for the last 30 days.
        # Input: self
        # Output: highest value for the last 30 days -> float
        values = [float(self.history[key]) for key in self.history]
        return max(values)

    def calculate_betha(self):
        # Calculate beta.
        # Input: self
        # Output: beta value -> float
        values = [float(self.history[key]) for key in self.history]
        avkastning_aktie = values[-1] / values[0]

        omx = [float(self.omx[key]) for key in self.omx]
        avkastning_omx = omx[-1] / omx[0]

        beta = avkastning_aktie / avkastning_omx

        return round(beta, 2)

    def __repr__(self):
        return f"{self.company_name} {self.debt_to_equity}  {self.pe}  {self.ps}"