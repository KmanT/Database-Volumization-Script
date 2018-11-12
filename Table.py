class Table:
    def __init__(self, tab_name, avg_rec_size, init_tab_size,):
        self.tab_name = tab_name
        self.avg_rec_size = avg_rec_size
        self.init_tab_size = init_tab_size

    def calc_volumization(self, overhead, growth_rate, num_years):
        answer = float(self.avg_rec_size) * float(self.init_tab_size)
        answer += answer * float(overhead)

        for i in range(1, num_years):
            answer += answer * float(growth_rate)

        return answer



