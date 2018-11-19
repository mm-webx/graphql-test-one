# graphql-test-one

save data:
```
mutation {
  createUser(name:"mm", lastName:"nn") {
    user {
      id,
      name,
      lastName
    }
  }
}
```

read data:
```
{
  users {
      id,
      name,
      lastName
    }
}
```