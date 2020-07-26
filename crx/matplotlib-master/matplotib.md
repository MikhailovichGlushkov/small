# Python可视化笔记



## 图像的结构

<img src="C:\Users\cultivator\Desktop\matplotlib-master\image-20200726190809802.png" alt="image-20200726190809802" style="zoom: 67%;" />

### 数据

### 从Excel中读取数据 read_excel():



* io : string, path object ; excel 路径。
* sheetname : string, int, mixed list of strings/ints, or None, default 0 返回多表使用sheetname=[0,1],若
* sheetname=None是返回全表 注意：int/string 返回的是dataframe，而none和list返回的是dict of dataframe
* header : int, list of ints, default 0 指定列名行，默认0，即取第一行，数据为列名行以下的数据 若数据不含列名，则设定 header = None
* skiprows : list-like,Rows to skip at the beginning，省略指定行数的数据
* skip_footer : int,default 0, 省略从尾部数的int行数据
* index_col : int, list of ints, default None指定列为索引列，也可以使用u”strings”
* names : array-like, default None, 指定列的名字。

```  python
import pandas as pd
import numpy as np
df = pd.read_excel('your/url'，header=none)
np_array = np.array(df)  #把读到的数据框处理成数组

```

### 从Excel中读取数据 read_excel():

### 一个基础线图

![Figure_1](C:\Users\cultivator\Desktop\matplotlib-master\Figure_1.png)

```  python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.05,10,1000)#10到100之间每隔0.05一个点
y = np.cos(x)
plt.plot(x,y,ls="-",lw=2,label="plot figure")
plt.legend()
plt.show()

```

* ls 线的类型
* lw线宽
* label数据标签

### 散点图

![Figure_2](C:\Users\cultivator\Desktop\matplotlib-master\Figure_2.png)




``` python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.05,10,1000)#10到100之间每隔0.05一个点
y = np.random.rand(1000) #生成1000个0~1之间的散点 1000是一维上数字的数量
plt.scatter(x,y,c="b",label="scatter figure")
plt.legend()
plt.show()
```

* c 颜色

### 细节线图

![Figure_5](C:\Users\cultivator\Desktop\matplotlib-master\Figure_5.png)

``` python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.05,10,1000)#10到100之间每隔0.05一个点
y = np.cos(x)
plt.plot(x,y,ls="-",c="r",lw=2,label="plot figure")
plt.xlim(0,12)
plt.ylim(-1,1)
plt.xlabel("横轴")
plt.ylabel("纵轴")
plt.legend()
plt.show()
```

