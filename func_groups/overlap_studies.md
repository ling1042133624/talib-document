# Overlap Studies Functions 重叠研究指标
### BBANDS - Bollinger Bands

> 函数名：BBANDS   
名称： 布林线指标  
简介：其利用统计原理，求出股价的标准差及其信赖区间，从而确定股价的波动范围及未来走势，利用波带显示股价的安全高低价位，因而也被称为布林带。    
分析和应用：
[百度百科](https://baike.baidu.com/item/bollinger%20bands/1612394?fr=aladdin) 
[同花顺学院](http://www.iwencai.com/yike/detail/auid/56d0d9be66b4f7a0?rid=53)   

```python
upperband, middleband, lowerband = BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
```

Learn more about the Bollinger Bands at [tadoc.org](http://www.tadoc.org/indicator/BBANDS.htm).  
### DEMA - Double Exponential Moving Average  双移动平均线

> 函数名：DEMA   
名称： 双移动平均线  
简介：两条移动平均线来产生趋势信号，较长期者用来识别趋势，较短期者用来选择时机。正是两条平均线及价格三者的相互作用，才共同产生了趋势信号。    
分析和应用：
[百度百科](https://baike.baidu.com/item/%E5%8F%8C%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF/1831921?fr=aladdin) 
[同花顺学院](http://www.iwencai.com/yike/detail/auid/a04d723659318237)   

```python
real = DEMA(close, timeperiod=30)
```

Learn more about the Double Exponential Moving Average at [tadoc.org](http://www.tadoc.org/indicator/DEMA.htm).  
### EMA - Exponential Moving Average

> 函数名：EMA   
名称： 指数平均数  
简介：是一种趋向类指标，其构造原理是仍然对价格收盘价进行算术平均，并根据计算结果来进行分析，用于判断价格未来走势的变动趋势。  
[百度百科](https://baike.baidu.com/item/EMA/12646151) 
[同花顺学院](http://www.iwencai.com/yike/detail/auid/b7a39d74783ad689?rid=589)   


NOTE: The ``EMA`` function has an unstable period.  
```python
real = EMA(close, timeperiod=30)
```

Learn more about the Exponential Moving Average at [tadoc.org](http://www.tadoc.org/indicator/EMA.htm).  
### HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
NOTE: The ``HT_TRENDLINE`` function has an unstable period.  

> 函数名：HT_TRENDLINE   here 到这里
名称： 希尔伯特瞬时变换  
简介：是一种趋向类指标，其构造原理是仍然对价格收盘价进行算术平均，并根据计算结果来进行分析，用于判断价格未来走势的变动趋势。  
[百度文库](https://wenku.baidu.com/view/0e35f6eead51f01dc281f18e.html) 

```python
real = HT_TRENDLINE(close)
```

`
**HT_TRENDLINE：深入瞬时趋势检测**

作为一名资深量化策略专家，我很乐意阐明 `talib.HT_TRENDLINE` 的细节，这是一个以跟踪**瞬时趋势**而闻名的技术指标。扣好安全带，这会变得非常有趣！

**核心机制：揭示希尔伯特变换**

`HT_TRENDLINE` 的魔力在于它利用了**希尔伯特变换 (HT)**。这种数学魔法提取了时间序列的**相位分量**，从本质上捕获了其趋势信息。简而言之，它就像一个棱镜，将价格数据分解为其趋势和周期分量。

**绘制趋势线：从相位到方向**

现在，提取的相位值不能直接解释。这就是 `HT_TRENDLINE` 发挥作用的地方。它对相位施加特定的缩放和平滑，最终生成一个**趋势线**，在零周围振荡。

* **正值：**表示**上升趋势**，表明价格序列高于其 HT 平滑的相位。
* **负值：**指向**下降趋势**，意味着价格序列低于其 HT 平滑的相位。

**读取信号：趋势确认和反转提示**

但这不仅仅是关于静态趋势标签。`HT_TRENDLINE` 在动态行为中表现出色：

* **趋势确认：**当价格序列始终保持在趋势线上方（下方）时，它会强化当前的上升（下降）趋势。
* **趋势反转提示：**当价格序列穿过趋势线时，它表明趋势方向可能发生转变。在相反方向的持续移动增加了反转信号的份量。

**记住：**

* `HT_TRENDLINE` 本质上是**反应性的**，最适合较短的交易时间框架。
* 与其他指标（如成交量或动量）结合使用可以提高信号的可靠性。
* 回测和优化对于根据您的特定市场和策略调整其参数至关重要。

**超越基础知识：**

* 探索 `HT_DCPHASE` 和 `HT_PHASOR` 等高级变体，以进行更深入的趋势和周期分析。
* 考虑使用诸如 `PyTaLib` 或 `ta-lib` 之类的库，以便在您选择的编程语言中方便地实现。

希望这个详细的解释为 `talib.HT_TRENDLINE` 提供了清晰的图像。随时提出您可能遇到的任何其他问题——量化分析的世界总是开放探索！

**关键要点**

* `HT_TRENDLINE` 是一种利用希尔伯特变换来跟踪瞬时趋势的技术指标。
* 它将价格序列分解为趋势和周期分量，然后生成一个趋势线，在零周围振荡。
* 正值趋势线表示上升趋势，负值趋势线表示下降趋势。
* 趋势线可以用于确认趋势或识别潜在的趋势反转。

**如何使用 HT_TRENDLINE**

`HT_TRENDLINE` 可以用于多种目的，包括：

* 确定趋势方向
* 确认趋势
* 识别趋势反转
* 制定交易策略

要使用 `HT_TRENDLINE`，您需要提供价格序列作为输入。您可以使用任何您喜欢的技术指标库来计算 `HT_TRENDLINE`。

以下是一个使用 `talib` 库计算 `HT_TRENDLINE` 的示例：

```python
import talib

# 获取价格序列
df = pd.read_csv("data.csv")

# 计算 HT_TRENDLINE
ht_trendline = talib.HT_TRENDLINE(df["close"])

# 绘制趋势线
plt.plot(df["date"], ht_trendline)
```

此示例将计算 `HT_TRENDLINE` 并将其绘制到图表中。您可以使用此信息来确定趋势

## HT_TRENDLINE 与 EMA：捕捉不同趋势的色调

HT_TRENDLINE 和 EMA 都是用于分析趋势的技术指标，但它们采用了截然不同的方法，并具有独特的优势：

**关键差异：**

* **重点：**
    * **HT_TRENDLINE：**跟踪**瞬时趋势**，揭示当前价格如何偏离其平滑趋势。
    * **EMA：**响应**近期价格变化**，提供平滑的趋势线，根据定义的加权方案适应价格变化。
* **计算：**
    * **HT_TRENDLINE：**使用**希尔伯特变换**，从价格序列的相位分量中提取趋势信息。
    * **EMA：**对过去价格应用**加权平均**，给最近的数据更高的权重，给较旧的数据更低的权重。
* **敏感度：**
    * **HT_TRENDLINE：**对即使是微小的价格波动也高度**敏感**，使其成为识别短期趋势转变的理想选择。
    * **EMA：**比简单移动平均线更**敏感**，但比 HT_TRENDLINE 敏感度低，在响应性和噪声消除之间提供了平衡。

**HT_TRENDLINE 的优势：**

* **早期趋势检测：**捕捉趋势方向的细微变化，潜在地在快速变化的市场中提供优势。
* **动态行为：**通过趋势线穿越和发散提供对趋势强度和潜在转折点的宝贵见解。
* **与其他指标互补：**与成交量或动量等趋势确认工具结合使用，可进行更强大的趋势分析。

**EMA 的优势：**

* **更平滑的趋势：**过滤掉噪声和短期波动，提供对潜在趋势方向的更清晰图像。
* **通用的时间框架：**根据选择的周期适应短期和长期分析。
* **广泛使用和理解：**适合所有级别交易员的熟悉且易于解释的指标。

**选择它们之间的区别：**

选择 HT_TRENDLINE 和 EMA 取决于您的具体交易需求和偏好：

* **对于短期、快速交易：**HT_TRENDLINE 的反应性和敏感性可能具有优势。
* **用于趋势确认和识别潜在反转：**HT_TRENDLINE 的动态行为提供了宝贵的见解。
* **用于更平滑的趋势识别和长期分析：**EMA 的过滤和通用性可能更受青睐。

归根结底，最好的方法是**尝试使用这两个指标**，并了解它们在您的交易策略中的优缺点。您甚至可以**将它们结合起来**，以获得更全面的市场视图！

请记住，没有一个指标是万无一失的，有效地解释趋势需要考虑各种因素并应用适当的风险管理。

希望这项比较能帮助您选择适合您的趋势追踪工作的正确工具！

**关键要点：**

* HT_TRENDLINE 和 EMA 都是用于分析趋势的技术指标。
* HT_TRENDLINE 专注于瞬时趋势，而 EMA 专注于近期价格变化。
* HT_TRENDLINE 更敏感，因此更适合识别短期趋势转变。EMA 更平滑，因此更适合识别长期趋势。
* 最佳选择取决于您的具体交易需求和偏好。
`



Learn more about the Hilbert Transform - Instantaneous Trendline at [tadoc.org](http://www.tadoc.org/indicator/HT_TRENDLINE.htm).  
### KAMA - Kaufman Adaptive Moving Average 考夫曼的自适应移动平均线

> 函数名：KAMA   
名称： 考夫曼的自适应移动平均线  
简介：短期均线贴近价格走势，灵敏度高，但会有很多噪声，产生虚假信号；长期均线在判断趋势上一般比较准确
，但是长期均线有着严重滞后的问题。我们想得到这样的均线，当价格沿一个方向快速移动时，短期的移动
平均线是最合适的；当价格在横盘的过程中，长期移动平均线是合适的。
> 

[参考1 -llq add](https://zhuanlan.zhihu.com/p/615114552) 

[参考2 -llq add](https://mp.weixin.qq.com/s?__biz=MzIxNzUyNTI4MA==&mid=2247484057&idx=1&sn=26a70a55b9191d178b1c15fdd2561bf9&chksm=97f93fd6a08eb6c04c2a129efe866664a52c63be66854fc886e455df4be726baa42fd387098c&scene=21#wechat_redirect) 

[参考1](http://blog.sina.com.cn/s/blog_62d0bbc701010p7d.html) 

[参考2](https://wenku.baidu.com/view/bc4bc9c59ec3d5bbfd0a7454.html?from=search)

NOTE: The ``KAMA`` function has an unstable period.  
```python
real = KAMA(close, timeperiod=30)
```

Learn more about the Kaufman Adaptive Moving Average at [tadoc.org](http://www.tadoc.org/indicator/KAMA.htm).  
### MA - Moving average  移动平均线

> 函数名：MA   
名称： 移动平均线  
简介：移动平均线，Moving Average，简称MA，原本的意思是移动平均，由于我们将其制作成线形，所以一般称之为移动平均线，简称均线。它是将某一段时间的收盘价之和除以该周期。 比如日线MA5指5天内的收盘价除以5 。  
[百度百科](https://baike.baidu.com/item/%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF/217887?fromtitle=MA&fromid=1511750#viewPageContent) 
[同花顺学院](http://www.iwencai.com/yike/detail/auid/a04d723659318237?rid=96)   


```python
real = MA(close, timeperiod=30, matype=0)
```

### MAMA - MESA Adaptive Moving Average
NOTE: The ``MAMA`` function has an unstable period.  
```python
mama, fama = MAMA(close, fastlimit=0, slowlimit=0)
```

Learn more about the MESA Adaptive Moving Average at [tadoc.org](http://www.tadoc.org/indicator/MAMA.htm).  
### MAVP - Moving average with variable period
```python
real = MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)
```

### MIDPOINT - MidPoint over period
```python
real = MIDPOINT(close, timeperiod=14)
```

Learn more about the MidPoint over period at [tadoc.org](http://www.tadoc.org/indicator/MIDPOINT.htm).  
### MIDPRICE - Midpoint Price over period
```python
real = MIDPRICE(high, low, timeperiod=14)
```

Learn more about the Midpoint Price over period at [tadoc.org](http://www.tadoc.org/indicator/MIDPRICE.htm).  
### SAR - Parabolic SAR  抛物线指标

> 函数名：SAR   
名称： 抛物线指标  
简介：抛物线转向也称停损点转向，是利用抛物线方式，随时调整停损点位置以观察买卖点。由于停损点（又称转向点SAR）以弧形的方式移动，故称之为抛物线转向指标    。  
[百度百科](https://baike.baidu.com/item/SAR/2771135#viewPageContent) 
[同花顺学院](http://www.iwencai.com/yike/detail/auid/d9d94e65be7f6b5e)   


```python
real = SAR(high, low, acceleration=0, maximum=0)
```

Learn more about the Parabolic SAR at [tadoc.org](http://www.tadoc.org/indicator/SAR.htm).  
### SAREXT - Parabolic SAR - Extended
```python
real = SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
```

### SMA - Simple Moving Average 简单移动平均线

> 函数名：SMA  
名称： 简单移动平均线  
简介：移动平均线，Moving Average，简称MA，原本的意思是移动平均，由于我们将其制作成线形，所以一般称之为移动平均线，简称均线。它是将某一段时间的收盘价之和除以该周期。 比如日线MA5指5天内的收盘价除以5 。  
[百度百科](https://baike.baidu.com/item/%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF/217887?fromtitle=MA&fromid=1511750#viewPageContent) 
[同花顺学院](http://www.iwencai.com/yike/detail/auid/a04d723659318237?rid=96)   


```python
real = SMA(close, timeperiod=30)
```

Learn more about the Simple Moving Average at [tadoc.org](http://www.tadoc.org/indicator/SMA.htm).  
### T3 - Triple Exponential Moving Average (T3) 三重指数移动平均线

> 函数名：T3  
名称：三重指数移动平均线  
简介：TRIX长线操作时采用本指标的讯号，长时间按照本指标讯号交易，获利百分比大于损失百分比，利润相当可观。 比如日线MA5指5天内的收盘价除以5 。  
[百度百科](https://baike.baidu.com/item/%E4%B8%89%E9%87%8D%E6%8C%87%E6%95%B0%E5%B9%B3%E6%BB%91%E5%B9%B3%E5%9D%87%E7%BA%BF/15749345?fr=aladdin) 
[同花顺学院](http://www.iwencai.com/yike/detail/auid/6c22c15ccbf24e64?rid=80)   



NOTE: The ``T3`` function has an unstable period.  
```python
real = T3(close, timeperiod=5, vfactor=0)
```

Learn more about the Triple Exponential Moving Average (T3) at [tadoc.org](http://www.tadoc.org/indicator/T3.htm).  
### TEMA - Triple Exponential Moving Average

> 函数名：TEMA（T3 区别？）
名称：三重指数移动平均线  


```python
real = TEMA(close, timeperiod=30)
```

Learn more about the Triple Exponential Moving Average at [tadoc.org](http://www.tadoc.org/indicator/TEMA.htm).  
### TRIMA - Triangular Moving Average
```python
real = TRIMA(close, timeperiod=30)
```

Learn more about the Triangular Moving Average at [tadoc.org](http://www.tadoc.org/indicator/TRIMA.htm).  
### WMA - Weighted Moving Average 移动加权平均法

> 函数名：WMA  
名称：加权移动平均线  
简介：移动加权平均法是指以每次进货的成本加上原有库存存货的成本，除以每次进货数量与原有库存存货的数量之和，据以计算加权平均单位成本，以此为基础计算当月发出存货的成本和期末存货的成本的一种方法。  
[百度百科](https://baike.baidu.com/item/%E7%A7%BB%E5%8A%A8%E5%8A%A0%E6%9D%83%E5%B9%B3%E5%9D%87%E6%B3%95/10056490?fr=aladdin&fromid=16799870&fromtitle=%E5%8A%A0%E6%9D%83%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87) 
[同花顺学院](http://www.iwencai.com/yike/detail/auid/262b1dfd1c68ee30)   


```python
real = WMA(close, timeperiod=30)
```

Learn more about the Weighted Moving Average at [tadoc.org](http://www.tadoc.org/indicator/WMA.htm).  

[Documentation Index](../doc_index.md)
[FLOAT_RIGHTAll Function Groups](../funcs.md)
