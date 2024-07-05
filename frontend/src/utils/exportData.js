import * as XLSX from 'xlsx';

import Papa from 'papaparse';
import { saveAs } from 'file-saver';

export function exportData(data, fileName, fileType) {
    const preparedData = data.map(row => {
        return {
          ...row,
          raw_json: JSON.stringify(row.raw_json)  // Convert raw_json to string
        };
      });
  if (fileType === 'csv') {
    exportToCSV(preparedData, fileName);
  } else if (fileType === 'excel') {
    exportToExcel(preparedData, fileName);
  }
}

function exportToCSV(data, fileName) {
  const csv = Papa.unparse(data);
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  saveAs(blob, `${fileName}.csv`);
}

function exportToExcel(data, fileName) {
  const ws = XLSX.utils.json_to_sheet(data);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
  const wbout = XLSX.write(wb, { bookType: 'xlsx', type: 'binary' });
  const buf = new ArrayBuffer(wbout.length);
  const view = new Uint8Array(buf);
  for (let i = 0; i < wbout.length; i++) view[i] = wbout.charCodeAt(i) & 0xFF;
  saveAs(new Blob([buf], { type: 'application/octet-stream' }), `${fileName}.xlsx`);
}
