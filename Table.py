class Table:
    def __init__(self, tab_name, avg_rec_size, init_tab_size,):
        self.tab_name = tab_name
        self.avg_rec_size = avg_rec_size
        self.init_tab_size = init_tab_size

    def calc_initial_volume(self, overhead):
        answer = float(self.avg_rec_size) * float(self.init_tab_size)
        answer += answer * float(overhead)

        return answer

    def calc_growth_volume(self, overhead, growth_rate, num_years):
        answer = self.calc_initial_volume(overhead, growth_rate, num_years)

        for i in range(1, num_years):
            answer += answer * float(growth_rate)

        #answer += answer * (growth_rate * num_years)

        return answer



