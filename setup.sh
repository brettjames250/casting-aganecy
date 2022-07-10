export FLASK_APP=app
export AUTH0_DOMAIN="casting-agency-brett.eu.auth0.com"
export ALGORITHMS="RS256"
export API_AUDIENCE="casting-agency"
export AUTH0_CALLBACK_URL="http://0.0.0.0:8080"
export AUTH0_CLIENT_ID="ROvStzhAFLT1Kxy9SQ86Fq9WTsfbWezV"
export DATABASE_URL="postgresql://postgres:password@localhost:5432/casting_agency"
#AUTH TOKENS - EXPIRE AFTER 1 DAY
export ASSISTANT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVxSi00SVk3VDdZZWNkY0NnMndEUCJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWJyZXR0LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM4NzY0NmE4ZWU5ZjFmZTFjODAyZjgiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTY1NzQ4MjMwMCwiZXhwIjoxNjU3NTY4NzAwLCJhenAiOiJST3ZTdHpoQUZMVDFLeHk5U1E4NkZxOVdUc2ZiV2V6ViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OiBhY3RvcnMiLCJnZXQ6IG1vdmllcyJdfQ.EuLxY1wiys9wnqv0j1_UFrXe1KY9tUFR6GWMfbWM9xxjLBjSjEedY1-MJ6A5gjSbBXx83vb4XWsjeuiGbc51CnAb_7m0fNdN4BDFmE0d8p4Qd8dFnS1NVc6EBgEeXQ9WlNhlTYN1S0qFYyjxIuEjZLVvum7EQEkAOSyu0hylHAgkKDmHcNn6WZ-KGu4_xyJF_wN8vV0bqfysa1YowPJF2EDJT_HQbTIVmaPyz7JaUXrbwO9Ey_rh0r6sWN2liJADF9NFxgRGvsQPOnW6TBI1IEu7hjTZ69Zhdk0r3afsUYPe2K0-R0X-RxFN_TVJL1AXNAyHs0HXEtUkFZAYwaJzNQ"
export DIRECTOR_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVxSi00SVk3VDdZZWNkY0NnMndEUCJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWJyZXR0LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM4NzZkYjExNzIzMDk2OWYwNWIxZTAiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTY1NzQ4MjI0MywiZXhwIjoxNjU3NTY4NjQzLCJhenAiOiJST3ZTdHpoQUZMVDFLeHk5U1E4NkZxOVdUc2ZiV2V6ViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOiBhY3RvcnMiLCJnZXQ6IGFjdG9ycyIsImdldDogbW92aWVzIiwicGF0Y2g6IGFjdG9ycyIsInBhdGNoOiBtb3ZpZXMiLCJwb3N0OiBhY3RvcnMiXX0.RU8lgQIEINdNZMWFuCb5jP2a1QAAVN0942QGMnr-yPpayUnQXTXZj6Lv0YudqHwQkXTOoz1OJhZ4SpfYizHwPjanKl_FUJ19Z9XqEgL8Ktib1QH4fhEcnTzicO8Sz7W0HwrleNQN0kOD68kdYDLzCXexOo0K0sydyzbr3CRGceQd4dpPu7pxsNXdIFzlGX8EE8QQET5kyF0eRrRN0Rzfuz14NFEJxC-uERYOhq33INcDhrodcin5yf4F8nJlL3MTwDH6vC2D4Wsf1cd24OO8QKtJmrKHIb8NtE727hX_dlH8_tmD0PPF43GlkiLYPgiDoQqFncXOxCK6LUSMq-z_3g"
export PRODUCER_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVxSi00SVk3VDdZZWNkY0NnMndEUCJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWJyZXR0LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM4NzUyY2QwZDkzNGJhZTVjZTljMTkiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTY1NzQ4MjE4NiwiZXhwIjoxNjU3NTY4NTg2LCJhenAiOiJST3ZTdHpoQUZMVDFLeHk5U1E4NkZxOVdUc2ZiV2V6ViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOiBhY3RvcnMiLCJkZWxldGU6IG1vdmllcyIsImdldDogYWN0b3JzIiwiZ2V0OiBtb3ZpZXMiLCJwYXRjaDogYWN0b3JzIiwicGF0Y2g6IG1vdmllcyIsInBvc3Q6IGFjdG9ycyIsInBvc3Q6IG1vdmllcyIsInBvc3Q6dGVzdCJdfQ.pS_OPSltEXTREilxhaN7Vs8i7tMZhjBIwUx_a1H6g0fLcioTXJR46opEvi2dFJVTKWbKl93SbQxTH7uTSJFsXSH_eOg5dImqSHGmfgjvQNoVz6dOLQ3CuJ79k-cl0fiLRpdDrcTtznJG51eWGSZTATu4grfuRzKqzsffZR6IRBqoXRdOEf0WwG9kJEKvOZKs5kNxZbGLPWx3BSY5RvSfBWYpkBQcQN-SdHZEQEYXOsSECJRfbZTHxuBKWfYYCpKdJnRZppX7Ue4d4Wyn322OiPAhDtUVPTViEImhhtMTK2H36m0TM1m3weIO0Xv5kgTBcxg6xBYq852nHKvo5tJ1EA"
export INVALID_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVxSi00SVk3VDdZZWNkY0NnMndEUCJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWJyZXR0LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM4NzUyY2QwZDkzNGJhZTVjZTljMTkiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTY1NzQ4MjE4NiwiZXhwIjoxNjU3NTY4NTg2LCJhenAiOiJST3ZTdHpoQUZMVDFLeHk5U1E4NkZxOVdUc2ZiV2V6ViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOiBhY3RvcnMiLCJkZWxldGU6IG1vdmllcyIsImdldDogYWN0b3JzIiwiZ2V0OiBtb3ZpZXMiLCJwYXRjaDogYWN0b3JzIiwicGF0Y2g6IG1vdmllcyIsInBvc3Q6IGFjdG9ycyIsInBvc3Q6IG1vdmllcyIsInBvc3Q6dGVzdCJdfQ.pS_OPSltEXTREilxhaN7Vs8i7tMZhjBIwUx_a1H6g0fLcioTXJR46opEvi2dFJVTKWbKl93SbQxTH7uTSJFsXSH_eOg5dImqSHGmfgjvQNoVz6dOLQ3CuJ79k-cl0fiLRpdDrcTtznJG51eWGSZTATu4grfuRzKqzsffZR6IRBqoXRdOEf0WwG9kJEKvOZKs5kNxZbGLPWx3BSY5RvSfBWYpkBQcQN-SdHZEQEYXOsSECJRfbZTHxuBKWfYYCpKdJnRZppX7Ue4d4Wyn322OiPAhDtUVPTViEImhhtMTK2H36m0TM1m3weIO0Xv5kgTBcxg6xBYq852nHKvo5tJ1EYT"



