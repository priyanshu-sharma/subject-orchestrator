# Subject Orchestrator
Responsible for managing course logistics

## Schema For Data Design

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
  id bigint
  name varchar
  department_id bigint
  schedule json
  meta json
}

Ref: sor.courses.department_id - sor.department.id

// Slot Domain

Table sor.slot {
  id bigint
  type varchar
  start_time datetime
  end_time datetime
}

Table sor.courses_slot {
  id uuid
  courses_id bigint
  slot_id bigint
  active boolean
  planned_capacity bigint
  actual_capacity bigint
}
Ref: sor.courses_slot.courses_id - sor.courses.id
Ref: sor.courses_slot.slot_id - sor.slot.id
```