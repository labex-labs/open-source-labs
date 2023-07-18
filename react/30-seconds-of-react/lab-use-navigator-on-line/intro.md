# Introduction

In this lab, we will learn how to use the `useNavigatorOnLine` hook in React to check whether a client is online or offline. We will create a function to get the online status of the client using the `Navigator.onLine` web API, use the `useState()` hook to create an appropriate state variable, and add listeners for appropriate events using the `useEffect()` hook to update the state and clean up those listeners when unmounting. Finally, we will return the online status state variable to display a message based on the current online status.
