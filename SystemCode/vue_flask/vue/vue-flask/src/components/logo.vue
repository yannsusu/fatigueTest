<template>
    <div class="logo">
      <!-- 其他内容 -->
      <img src="@/assets/logo.png" alt="Logo" class="logo">
      <!-- 其他内容 -->
    </div>
</template>
  
  <style>
  .logo-container {
    position: relative; /* 确保容器是相对定位，以便容器内部的绝对定位生效 */
  }
  
  .logo {
    position: absolute;
    top: 10px; /* 距离容器顶部的距离，根据需要进行调整 */
    left: 10px; /* 距离容器左侧的距离，根据需要进行调整 */

    /* 添加缩放样式 */
    max-width: 200px; /* 设置图标最大宽度，防止图标过大 */
    max-height: 100px; /* 设置图标最大高度，防止图标过大 */
    opacity: 0.9; /* 设置透明度为50% */
  }
  </style>
  