list_marks_in_classes_in_shool_8=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [4,4,4,4]}, {'school_class': '8b', 'scores': [5,5,5,5]}]

def avg_marks (list_marks_in_classes):
    try:
        list_sum_marks_in_classes = []
        list_len_marks_in_classes = []
        for list_marks in list_marks_in_classes:
            marks = list_marks.get('scores')
            name_class = list_marks.get('school_class')
            sum_marks_in_class = sum(marks)
            len_marks_in_class = len(marks)
            avg_marks_in_class = sum_marks_in_class/len_marks_in_class
            list_sum_marks_in_classes.append(sum_marks_in_class)
            list_len_marks_in_classes.append(len_marks_in_class)
            print('Средняя оценка по классу {} = {}'.format(name_class, avg_marks_in_class))
        summ_all_marks_in_shool = float(sum(list_sum_marks_in_classes))
        count_all_marks_in_shool = float(sum(list_len_marks_in_classes))
        avg_all_marks_in_shool = round(summ_all_marks_in_shool/count_all_marks_in_shool,2)
        return avg_all_marks_in_shool
    except (TypeError,AttributeError):
        print('Неверный тип данных')

if __name__ == '__main__':
    avg_marks_in_shool=avg_marks(list_marks_in_classes_in_shool_8)
    print('Средняя оценка по школе = {}'.format(avg_marks_in_shool))