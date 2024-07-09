# Price Transform Functions



### 这类指标的作用用来代替close价格的作用，因为通常的close价格并不能很好的代表bar的所有信息，用这类指标处理过的价格可以作为阶段性的信息，比单一的close价更能体现价格。



### AVGPRICE - Average Price
> 函数名：AVGPRICE   
名称：平均价格函数
```python
real = AVGPRICE(open, high, low, close)
```

Learn more about the Average Price at [tadoc.org](http://www.tadoc.org/indicator/AVGPRICE.htm).  

### MEDPRICE - Median Price
> 函数名：MEDPRICE   
名称：中位数价格
```python
real = MEDPRICE(high, low)
```

Learn more about the Median Price at [tadoc.org](http://www.tadoc.org/indicator/MEDPRICE.htm).  
### TYPPRICE - Typical Price
> 函数名：TYPPRICE   
名称：代表性价格

```python
real = TYPPRICE(high, low, close)
```

Learn more about the Typical Price at [tadoc.org](http://www.tadoc.org/indicator/TYPPRICE.htm).  
### WCLPRICE - Weighted Close Price
> 函数名：WCLPRICE   
名称：加权收盘价

```python
real = WCLPRICE(high, low, close)
```

Learn more about the Weighted Close Price at [tadoc.org](http://www.tadoc.org/indicator/WCLPRICE.htm).  

[文档](../doc_index.md)
[FLOAT_RIGHTAll Function Groups](../funcs.md)
