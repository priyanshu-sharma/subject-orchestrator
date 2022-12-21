# subject-orchestrator
Responsible for managing course logistics

```
Table sor.user_tracking {
  created_by_id bigint
  update_by_id bigint
}

Table sor.auto_timestamped {
  install_ts datetime
  update_ts datetime
}

Table sor.school {
  id bigint
  name varchar
  state varchar
  country varchar
  college_name varchar
  type varchar
  meta json
  active boolean
}

Table sor.department {
  id bigint
  name varchar
  school_id bigint
  meta json
  active boolean
}

Ref: sor.department.school_id - sor.school.id


Table sor.courses {
  id uuid
  name varchar
  department_id bigint
  meta json
  planned_capacity bigint
  actual_capacity bigint
}

Ref: sor.courses.department_id - sor.department.id

```