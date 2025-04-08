<template>
    <div class="logo">
      <!-- Other Contents -->
      <img src="@/assets/logo.png" alt="Logo" class="logo">
      <!-- Other COntents -->
    </div>
</template>
  
  <style>
  .logo-container {
    position: relative; /* Make sure the container is relatively positioned so that absolute positioning inside the container takes effect */
  }
  
  .logo {
    position: absolute;
    top: 10px; /* Distance from the top of the container, adjusted as necessary */
    left: 10px; /* Distance from the left side of the container, adjusted as needed */

    /* Adding Zoom Styles */
    max-width: 200px; /* Set the maximum icon width to prevent the icon from being too large */
    max-height: 100px; /* Set the maximum height of the icon to prevent the icon from being too large */
    opacity: 0.9; /* Set transparency to 50 per cent */
  }
  </style>
  
  