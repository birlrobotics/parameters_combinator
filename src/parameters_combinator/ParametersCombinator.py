class ParametersCombinator(object):
    def __init__(self, _dict_of_params):
        import copy
        from ListOfParams import ListOfParams

        dict_of_params = copy.deepcopy(_dict_of_params)

        for key, value in dict_of_params.iteritems():
            if type(value) != ListOfParams:
                tmp = ListOfParams()
                tmp.append(value)
                dict_of_params[key] = tmp

        self.dict_of_params = dict_of_params


    def iteritems(self):
        dict_of_params = self.dict_of_params
        keys = []
        values = []
        for key, value in dict_of_params.iteritems():
            keys.append(key)
            values.append(value)
        max_height = len(keys)
        stack = [-1]
        while True:
            stack_height = len(stack)
            if stack_height == 0:
                break
            elif stack_height > max_height:
                yield dict([(keys[i], values[i][stack[i]]) for i in range(max_height)])
                stack.pop()
            else:
                stack[-1] += 1
                v_top = stack[-1]
                if v_top < len(values[stack_height-1]):
                    stack.append(-1)
                else:
                    stack.pop()

    def get_all_combinations(self):
        return list(self.iteritems())

if __name__ == '__main__':
    from parameters_combinator import ParametersCombinator
    from parameters_combinator import ListOfParams
    dict_of_params = {
        'n_components': ListOfParams([3,5,7]),
        'covariance_type': ListOfParams(['diag', 'spherical', 'full', 'tied']),
        'n_iter': 1000,
    }
    pc = ParametersCombinator(dict_of_params)
    for i in pc.iteritems():
        print i

    print pc.get_all_combinations()
