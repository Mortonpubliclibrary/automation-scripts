for /F "tokens=3 delims=: " %%H in ('sc query lptclient ^| findstr "        STATE"') do (
  if /I "%%H" NEQ "RUNNING" (
   net start lptclient
  )
)
