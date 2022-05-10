## Java基础

### 11 Java jdk 介绍

Java运行机制及运行过程
- .java ->编译 .class ->运行（操作系统JVM虚拟机）
  - JVM负责执行指令，管理数据、内存、寄存器。

### 35 变量

Java变量基本要素（类型+名称+值）

### 40 数据类型

**Java数据类型**： 
- 基本数据类型：数值型，字符型，布尔型
- 引用数据类型：类class，接口interface，数组([])

### 156 数组必要性
- 定义一个数组：double[] hens = (3, 5, 1}; 或 double hens[] = {3, 5, 1};
- 数组的定义
  - 动态初始化 int a[] = new int[5] new在堆里申请内存
  - 动态初始化 先声明数组再创建数组 int a[]; a = new int[10];
  - 静态初始化 如果知道数组有多少元素
- 数组属于引用类型，数组型数据是对象（object）

### 166 数组拷贝
- 要求数据空间是独立的

### 169 数组扩容

## 面向对象编程

### 192 类与对象

单独变量解决，不利于数据的管理。

- 对象[属性,行为]

### 195 对象内存布局

- 栈内存对象名/对象引用
- 堆内存对象-地址（字符串）和基本数据类型
- 字符串引用类型存在方法区常量池

在方法区加载类的信息（属性信息，行为）
- 访问修饰符 protected/public/private

### 200 对象创建过程

- 栈：存放基本数据类型
- 堆：存放对象
- 方法区：常量池，类加载信息

### 201 成员方法

- 访问修饰符（控制方法的使用范围）

### 227 方法重载

### 234 可变参数

Java允许将同一个类中多个同名同功能但参数个数不同的方法，封装成一个方法。
- public int sum(int... nums){}

### 236 作用域

- 属性和局部变量

### 240 构造器Constructor

构造器是类的一种特殊方法，主要作用时对新对象的初始化。
- 如果没有定义构造器，系统会自动给类生成一个默认无参构造器。

### 245 this

java虚拟机会给每个对象分配this，代表当前对象。

### 273 包

包的作用
- 区分相同名字的类
- 当类很多时，可以很好的管理类（看Java API文档）
- 控制访问范围

包的基本语法
- package表示打包
- com.hspedu表示包名


