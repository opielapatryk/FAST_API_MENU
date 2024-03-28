# FAST API MENU
## Project is created based on Clean Architecture <br>
### Inward -> Simple data x Outward -> Interfaces

## External systems
Web Framework: Fast API <br>
Repository: Memory <br>

## Gateways
Dictionary + DB Interface <br>
i.e. class MemRepo <br>

## Use Cases: "business logic"
### Receive repo + parameters, returns results
GET: List all dishes <br>
GET{id}: List dish <br>
POST: Add dish <br>
PUT: Edit dish <br>
DELETE: Remove dish <br>

## Entities
Module: Dish <br>

# TODO
- [] Apply Clean Architecture <br> 
- [] Layer Abstraction<br> 
- [] Dependency Injection<br> 
- [] UseCase Implementation<br> 
- [] Serialization / Deserialization<br> 
- [] Mock Repo Implementation<br>  
- [] Database with SQLAlchemy<br> 
- [] Apply Tests<br> 
