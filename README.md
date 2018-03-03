# parameters_combinator

# Demo

```python
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
```

Output:
```python
{'n_iter': 1000, 'n_components': 3, 'covariance_type': 'diag'}
{'n_iter': 1000, 'n_components': 3, 'covariance_type': 'spherical'}
{'n_iter': 1000, 'n_components': 3, 'covariance_type': 'full'}
{'n_iter': 1000, 'n_components': 3, 'covariance_type': 'tied'}
{'n_iter': 1000, 'n_components': 5, 'covariance_type': 'diag'}
{'n_iter': 1000, 'n_components': 5, 'covariance_type': 'spherical'}
{'n_iter': 1000, 'n_components': 5, 'covariance_type': 'full'}
{'n_iter': 1000, 'n_components': 5, 'covariance_type': 'tied'}
{'n_iter': 1000, 'n_components': 7, 'covariance_type': 'diag'}
{'n_iter': 1000, 'n_components': 7, 'covariance_type': 'spherical'}
{'n_iter': 1000, 'n_components': 7, 'covariance_type': 'full'}
{'n_iter': 1000, 'n_components': 7, 'covariance_type': 'tied'}
```
