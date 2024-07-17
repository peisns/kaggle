# csv 라이브러리 가져오기
# import csv

# pandas 라이브러리 가져오기
import pandas as pd

# CSV load
data = pd.read_csv("customer_purchase_data.csv")

# csv 라이브러리로 csv 읽어보기
with open("customer_purchase_data.csv", mode="r") as file:
    # reader = csv.reader(file)
    # print("reader:", reader)
    # reader: <_csv.reader object at 0x1........>
    # print("-" * 60)
    # for row in reader:
        # print(row)
        """
        ['67', '1', '28775.331068896852', '18', '2', '17.625707203046694', '0', '1', '1']
        ['40', '1', '57363.247540525364', '7', '4', '12.20603320759119', '0', '0', '0']
        ['63', '0', '134021.77553236455', '16', '2', '37.31163380267996', '1', '0', '1']
        ['50', '0', '52625.66597423874', '13', '0', '25.348016654369804', '1', '4', '1']
        """
        # print("=" * 60)


# pandas로 csv 읽어보기
data = pd.read_csv("customer_purchase_data.csv")
# print(data)
"""
      Age  Gender  ...  DiscountsAvailed  PurchaseStatus
0      40       1  ...                 5               1
1      20       1  ...                 5               0
2      27       1  ...                 0               1
3      24       1  ...                 4               1
4      31       1  ...                 0               1
...   ...     ...  ...               ...             ...
1495   39       1  ...                 5               1
1496   67       1  ...                 1               1
1497   40       1  ...                 0               0
1498   63       0  ...                 0               1
1499   50       0  ...                 4               1

[1500 rows x 9 columns]
"""

# 데이터 구조 확인
# data.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1500 entries, 0 to 1499
Data columns (total 9 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Age                 1500 non-null   int64  
 1   Gender              1500 non-null   int64  
 2   AnnualIncome        1500 non-null   float64
 3   NumberOfPurchases   1500 non-null   int64  
 4   ProductCategory     1500 non-null   int64  
 5   TimeSpentOnWebsite  1500 non-null   float64
 6   LoyaltyProgram      1500 non-null   int64  
 7   DiscountsAvailed    1500 non-null   int64  
 8   PurchaseStatus      1500 non-null   int64  
dtypes: float64(2), int64(7)
memory usage: 105.6 KB
"""

# 데이터 샘플 확인
# print(data.head(5))
"""
   Age  Gender   AnnualIncome  NumberOfPurchases  ...  TimeSpentOnWebsite  LoyaltyProgram  DiscountsAvailed  PurchaseStatus
0   40       1   66120.267939                  8  ...           30.568601               0                 5               1
1   20       1   23579.773583                  4  ...           38.240097               0                 5               0
2   27       1  127821.306432                 11  ...           31.633212               1                 0               1
3   24       1  137798.623120                 19  ...           46.167059               0                 4               1
4   31       1   99300.964220                 19  ...           19.823592               0                 0               1

[5 rows x 9 columns]
"""

# 데이터 기초통계 확인
# print(data.describe())
"""
               Age       Gender   AnnualIncome  NumberOfPurchases  ...  TimeSpentOnWebsite  LoyaltyProgram  DiscountsAvailed  PurchaseStatus
count  1500.000000  1500.000000    1500.000000        1500.000000  ...         1500.000000     1500.000000       1500.000000      1500.00000
mean     44.298667     0.504667   84249.164338          10.420000  ...           30.469040        0.326667          2.555333         0.43200
std      15.537259     0.500145   37629.493078           5.887391  ...           16.984392        0.469151          1.705152         0.49552
min      18.000000     0.000000   20001.512518           0.000000  ...            1.037023        0.000000          0.000000         0.00000
25%      31.000000     0.000000   53028.979155           5.000000  ...           16.156700        0.000000          1.000000         0.00000
50%      45.000000     1.000000   83699.581476          11.000000  ...           30.939516        0.000000          3.000000         0.00000
75%      57.000000     1.000000  117167.772858          15.000000  ...           44.369863        1.000000          4.000000         1.00000
max      70.000000     1.000000  149785.176481          20.000000  ...           59.991105        1.000000          5.000000         1.00000

[8 rows x 9 columns]
"""

# 결측값 확인
missing_value = data.isnull().sum()
# data.isnull()
# data내의 각 요소가 결측값인지 여부를 판단하는 메서드
# 결측값인 경우 True, 결측값이 아닌 경우 False를 반환
# .sum()
# isull() 메서드가 반환한 불리언 값을 각 열을 기준으로 True 수 합계를 계산한다
# True는 1로 간주된다
# print("missing_value:\n", missing_value)
"""
missing_value:
 Age                   0
Gender                0
AnnualIncome          0
NumberOfPurchases     0
ProductCategory       0
TimeSpentOnWebsite    0
LoyaltyProgram        0
DiscountsAvailed      0
PurchaseStatus        0
dtype: int64
"""

# numpy 라이브러리가져오기
import numpy as np

# 결측값 변환 함수
def add_missing_values(df, col_name, missing_frac):
    """
    특정 열에 지정된 비율의 결측값을 추가합니다.

    :param df: 데이터프레임
    :param col_name: 결측값을 추가할 열 이름
    :param missing_frac: 결측값 비율 (0.0 ~ 1.0)
    """
    np.random.seed(42)  # 재현성을 위해 랜덤 시드 설정
    # random.seed()메서드는 난수 생성기의 시드를 설정하는데 사용됨
    # 시드를 설정함으로써 난수 생성 과정의 초기 상태를 결정할 수 있고,
    # 이를 통해 동일한 난수 시퀀스를 얻을 수 있음

    n_rows = df.shape[0]  # 데이터프레임의 행 수
    # (행의 수, 열의 수) 형태의 튜플을 반환함
    # 예를 들어 1500개의 데이터와 5개의 데이터 프레임이 있다면, df.shape는 (int, int)형태, (5, 1500)을 반환
    # print("n_rows:", n_rows)
    
    n_missing = int(n_rows * missing_frac)  # 결측값을 추가할 행의 수를 계산
    # 1500개 * 결측값 비율(0.0)

    missing_indices = np.random.choice(n_rows, n_missing, replace=False)
    # 결측값을 추가할 행의 인덱스를 무작위로 선택
    # 랜덤으로.선택(int, int, replace:Bool)
    # a로 정수를 전달할 경우 0부터 n-1까지의 범위에서 무작위 선택을 수행함
    # a로 배열을 전달할 경우 배열에서 무작위로 요소를 선택함
    # size로 몇개나 무작위로 선택할 지 설정
    # replace 인자를 통해 중복을 허용하지 않음을 설정
    # print("missing_indices:", missing_indices)
    # missing_indices: [1116 1368  422  413  451 ... 694 1001  322  782]
    
    df.loc[missing_indices, col_name] = np.nan  # 선택된 인덱스의 열 값을 NaN으로 설정
    # loc는 라벨 기반 인덱싱으로 특정 행과 열에 접근하거나 값을 설정할 수 있도록 함
    # DataFrame.loc[row_indexer, column_indexer]의 경우에
    # 각각 선택할 행, 열의 라벨 또는 라벨의 리스트, 슬라이스, 불리언 배열 등이 인자로 전달됨


add_missing_values(data, 'Age', 0.1)  # Age 열에 10% 결측값 추가
add_missing_values(data, 'Gender', 0.1)  # Gender 열에 10% 결측값 추가

print("Data with missing values:\n", data.tail(10))
print("Missing values count:\n", data.isnull().sum())

age_mean = data['Age'].mean()
print("Age Mean: ", age_mean)
# Age Mean:  44.404444444444444

# 데이터 전처리 - 결측값 처리(평균값으로 대체)
data['Age'].fillna(age_mean, inplace=True)
# inplace: bool은 원래 데이터 프레임을 변경하는지 여부, False라면 새로운 데이터 프레임을 반환함
print(data.isnull().sum())

print(data.tail(10))

gender_mode = data['Gender'].mode()[0]
print("gender_mode:", gender_mode)

# 범주형 데이터 전처리 - 결측값 처리 (최빈값으로 대체)
data['Gender'].fillna(gender_mode, inplace=True)

print("Missing values count:\n", data.isnull().sum())

print("Gender is Male or Female")
print(data['Gender'].head())
print("Male is 0, Female is 1")
data['Gender'] = ['Male' if gender == 0 else 'Female' for gender in data['Gender']]
print(data['Gender'].head())
