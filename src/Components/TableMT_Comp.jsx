import React from "react";
import MaterialTable, { MTableBodyRow, MTablePagination } from "material-table";
import { useState } from "react";
import { useRef } from "react";
import { Button, createStyles, makeStyles, TablePagination, withStyles } from "@material-ui/core";

function createData(school, participants, pass_exam, enroll, location) {
  return {
    school: school,
    participants: participants,
    pass_exam: pass_exam,
    enroll: enroll,
    location: location
  };
}

const rows = [
  createData("A", 100, 100, 100, "Jl."),
  createData("B", 45, 10, 1),
  createData("C", 76, 70, 68),
  createData("D", 87, 66, 59),
  createData("E", 10, 5, 4),
  createData("F", 130, 20, 20),
  createData("G", 55, 30, 20),
  createData("H", 250, 98, 76),
  createData("I", 178, 30, 10),
  createData("J", 90, 80, 80),
];

const customCheckBoxColor = makeStyles({
  root: {
    color: "#FF9198",
    "&$checked": {
      color: "#FF9198",
    },
  },
  checked: {},
});

function createState() {
  let st = {};
  for (let i = 0; i < rows.length; i++) {
    st = {
      ...st,
      i: false,
    };
  }
  return st;
}

function TableMT(props) {
  console.log(props.data)
  const classes = customCheckBoxColor();
  const [rowState, setRow] = useState(createState());
  const [selection, setSelection] = useState(createState());
  const tableRef = useRef(null);

  const updateRows = (rows) => {
    let updatedRow = {};
    rows.every((row) => {
      updatedRow = {
        ...updatedRow,
        [row.tableData.id]: true,
      };
      return true;
    });
    setSelection({
      ...updatedRow,
    });
  };

  const updateRow2 = (rowData) => {
    setRow({
      [rowData.tableData.id]: rowState[rowData.tableData.id] ? !rowState[rowData.tableData.id]  : true,
    });
  };

  const isDisabled = (rowData) => {
    console.log(rowData);
    return {
      disabled: false,
      color: "primary",
    };
  };

  return (
    <>
      <MaterialTable
        data={props.data}
        columns={[
          //{ title: '', render: rowData=> <input disabled={Object.keys(rowState).length>=5} type="checkbox"/>, disableClick: true},
          { title: "Sekolah", field: "V_NAMA_SMTA" },
          { title: "Total Partisipan", field: "TOTAL" },
          { title: "Total Partisipan Lulus", field: "PASS" },
          { title: "Total Daftar Ulang", field: "ENROLL" },
        ]}
        title={props.title}
        style={{
          width: "1000px",
        }}
        // components={{
        //   Row: (props) => (
        //     <MTableBodyRow
        //       className={rowState[parseInt(props.index)] ? "active" : ""}
        //       {...props}
        //     />
        //   ),
        // }}
        options={{
          selection: true,
          toolbar: false,
          selectionProps: (rowData) => ({
            disabled:
              !rowData.tableData.checked && Object.keys(selection).length >= 5,
            className: classes.root,
          }),
          showSelectAllCheckbox: false,
          emptyRowsWhenPaging: false,
        }}
        onSelectionChange={(rows) => updateRows(rows)}
        // onRowClick={(event, rowData) => {
        //   event.preventDefault();
        //   updateRow2(rowData)
        // }}
        tableRef={tableRef}
      />
      <Button onClick={() => tableRef.current.onAllSelected(false)}>
        Reset
      </Button>
    </>
  );
}

export default TableMT;
