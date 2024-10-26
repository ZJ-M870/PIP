# 机器人测距的主要方法

## 一、激光测距

### 1、脉冲测距法

```cpp
distance = SPEED_0F_LIGHT × (interval_time) / 2
```

## 二、超声波测距

```cpp
distance = (1/2) × SOUND_VELOCITY × interval_time
```

## 三、视觉测距

### 1、三角测距法

```cpp
distance = (actual_width × focal_length) / pixel_width
```

### 2、立体视觉测距法

```cpp
distance = (focal_length × camera_spacing) / (corresponding_point_position_1 - corresponding_point_position_2)
```

# 难点

*   激光测距以及超声波测距如何完全确定到机器人的中心位置
*   能否对机器人下一个时刻做出一定的预判以确保获得精确位置（不清楚是否需要一直追踪）
*   面对不同学校设计的不同机器人我方视觉的模型能否稳定的识别

